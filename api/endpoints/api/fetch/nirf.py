import inspect
import uuid
from mayim import Mayim
from sanic import Request, json
from sanic.views import HTTPMethodView
from sanic.log import logger

from api.decorators.require_login import require_login
from api.mayim.nirf_executor import NIRFExecutor
from api.models.internal.jwt_data import JWT_Data


class NIRFFetch(HTTPMethodView):
    @require_login()
    async def get(self, request: Request, jwt_data: JWT_Data, slug: str):
        executor = Mayim.get(NIRFExecutor)

        methods = {
            method_name.replace("get_NIRF_", ""): method
            for method_name, method in inspect.getmembers(
                executor, predicate=inspect.ismethod
            )
            if method_name.startswith("get_NIRF_")
        }

        if not slug:
            return json(
                {
                    method: str(
                        inspect.signature(getattr(NIRFExecutor, f"get_NIRF_{method}"))
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
            method = getattr(NIRFExecutor, f"get_NAAC_{slug}")
            call = getattr(executor, f"get_NAAC_{slug}")

            required_args = inspect.signature(method)

            if len(required_args.parameters) > 1 and not args:
                return json(
                    {
                        "error": "Bad Request",
                        "message": "This format requires additional arguments.",
                    },
                    400,
                )
            data = await call(**args) if required_args.parameters else await call()
            if not data:
                return json({"data": []})
            return json({"data": [d.to_dict() for d in data]})
        except Exception as e:
            ref_id = uuid.uuid4()
            logger.error(
                f"REF ID: {ref_id}\nAn error occurred while fetching NAAC data: {str(e)}",
                exc_info=e,
            )
            return json(
                {"error": "Internal Server Error", "reference_id": str(ref_id)}, 500
            )
