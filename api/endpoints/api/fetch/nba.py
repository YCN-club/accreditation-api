import inspect
from typing import List, TypeVar
import uuid
from mayim import Mayim
from sanic import Request, json
from sanic.views import HTTPMethodView
from sanic.log import logger

from api.decorators.require_login import require_login
from api.mayim.nba_executor import NBAExecutor
from api.models.generic_model import GenericModel
from api.models.internal.jwt_data import JWT_Data

T = TypeVar("T", bound=GenericModel)


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
            return json(
                {
                    method: str(
                        inspect.signature(getattr(NBAExecutor, f"get_NBA_{method}"))
                    )
                    .replace("self, ", "")
                    .replace("self", "")
                    for method in methods
                }
            )

        if slug not in methods:
            return json(
                {
                    "error": "Not Found",
                    "message": "The requested format is not available.",
                },
                404,
            )

        try:
            args = request.json if request.json else {}
            method = getattr(NBAExecutor, f"get_NAAC_{slug}")
            call = getattr(executor, f"get_NAAC_{slug}")

            required_args = inspect.signature(method)
            needs_args = len(required_args.parameters) > 1

            if needs_args and not args:
                return json(
                    {
                        "error": "Bad Request",
                        "message": "This format requires additional arguments.",
                    },
                    400,
                )
            data: List[T] = await call(**args) if needs_args else await call()
            if not data:
                return json({"data": []})
            return json({"data": [d.to_dict() for d in data]})
        except Exception as e:
            ref_id = uuid.uuid4()
            logger.error(
                f"REF ID: {ref_id}\nAn error occurred while fetching NBA data: {str(e)}",
                exc_info=e,
            )
            return json(
                {"error": "Internal Server Error", "reference_id": str(ref_id)}, 500
            )
