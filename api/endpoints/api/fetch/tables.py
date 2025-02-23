import inspect
from mayim import Mayim
from sanic import Request, json
from sanic.views import HTTPMethodView

from api.decorators.require_login import require_login
from api.mayim.table_executor import TableExecutor
from api.models.internal.jwt_data import JWT_Data


class TablesRoot(HTTPMethodView):
    @require_login()
    async def get(self, request: Request, jwt_data: JWT_Data, slug: str):
        # Get Executor
        executor = Mayim.get(TableExecutor)

        # Protected Tables
        protected_tables = ["auth"]

        methods = {
            method_name.replace("fetch_", ""): method
            for method_name, method in inspect.getmembers(
                executor, predicate=inspect.ismethod
            )
            if method_name.startswith("fetch_")
        }

        # Remove protected tables
        for table in protected_tables:
            methods.pop(table, None)

        if not slug:
            return json({"methods": [method for method in methods]})

        if slug not in methods:
            return json(
                {
                    "error": "Not Found",
                    "message": "The requested table is not available.",
                },
                404,
            )

        # Get query args
        columns = request.args.get("columns", None)

        # Fetch data
        db_data = await getattr(executor, f"fetch_{slug}")()
        data = [d.to_dict() for d in db_data]

        # Filter columns
        if columns:
            cols = columns.split(",")
            resp = [{k: v for k, v in d.items() if k in cols} for d in data]
            return json({"data": resp})
        return json({"data": data})
