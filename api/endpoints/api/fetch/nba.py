import inspect
from mayim import Mayim
from sanic import Request, json
from sanic.views import HTTPMethodView

from api.decorators.require_login import require_login
from api.mayim.nba_executor import NBAExecutor
from api.models.internal.jwt_data import JWT_Data


class NBAFetch(HTTPMethodView):
    @require_login()
    async def get(self, request: Request, jwt_data: JWT_Data, slug: str):
        executor = Mayim.get(NBAExecutor)

        methods = {
            method_name.replace("get_NBA_", ""): method
            for method_name, method in inspect.getmembers(
                executor, predicate=inspect.ismethod
            )
            if method_name.startswith("get_NBA_")
        }

        if not slug:
            return json({"options": list(methods.keys())})

        if slug not in methods:
            return json(
                {
                    "error": "Not Found",
                    "message": "The requested format is not available.",
                },
                404,
            )

        # TODO: Dynamically call the method
        return json({"message": "Not implemented yet."})
