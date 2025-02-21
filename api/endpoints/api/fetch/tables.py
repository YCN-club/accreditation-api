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

        # Get query args
        columns = request.args.get("columns", "").split(",")

        # Fetch data
        db_data = await getattr(executor, f"fetch_{slug}")()
        data = [d.to_dict() for d in db_data]

        # Filter columns
        if columns:
            resp = [{k: v for k, v in d.items() if k in columns} for d in data]
            return json({"data": resp})
        return json({"data": data})
