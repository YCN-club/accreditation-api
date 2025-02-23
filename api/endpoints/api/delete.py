import inspect
import uuid
from datetime import datetime

from mayim import Mayim
from sanic import Request, json
from sanic.log import logger
from sanic.views import HTTPMethodView

from api.decorators.require_login import require_login
from api.mayim.delete_executor import DeleteExecutor
from api.models.internal.jwt_data import JWT_Data


class DeleteRoot(HTTPMethodView):
    @require_login()
    async def get(self, request: Request, jwt_data: JWT_Data, slug: str):

        executor = Mayim.get(DeleteExecutor)

        methods = (
            method_name.replace("delete_", "")
            for method_name, _ in inspect.getmembers(
                executor, predicate=inspect.ismethod
            )
            if method_name.startswith("delete_")
        )

        if not slug:
            return json(
                {
                    method: {
                        "args": str(
                            inspect.signature(
                                getattr(DeleteExecutor, f"delete_{method}")
                            )
                        )
                        .replace("self, ", "")
                        .replace("self", "")
                        .split(" -> ")[0],
                    }
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
            method = getattr(DeleteExecutor, f"delete_{slug}")
            call = getattr(executor, f"delete_{slug}")

            required_args = inspect.signature(method)
            needs_args = len(required_args.parameters) > 1

            # Set default year to current year if not provided
            # Specific check in required_args as year may be a substring of another argument
            if "year: int" in str(required_args):
                args["year"] = int(args.get("year", datetime.now().year))

            if needs_args and not args:
                return json(
                    {
                        "error": "Bad Request",
                        "message": "This format requires additional arguments.",
                    },
                    400,
                )
            await call(**args) if needs_args else await call()
        except Exception as e:
            ref_id = uuid.uuid4()
            logger.error(
                f"REF ID: {ref_id}\nAn error occurred while fetching deleting data: {str(e)}",
                exc_info=e,
            )
            return json(
                {"error": "Internal Server Error", "reference_id": str(ref_id)}, 500
            )
