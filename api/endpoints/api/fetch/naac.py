from datetime import datetime
import inspect
from typing import List, TypeVar
import uuid
from mayim import Mayim
from sanic import Request, json
from sanic.views import HTTPMethodView
from sanic.log import logger

from api.decorators.require_login import require_login
from api.mayim.naac_executor import NAACExecutor
from api.models.generic_protocol import GenericProtocol
from api.models.internal.jwt_data import JWT_Data

T = TypeVar("T", bound=GenericProtocol)


class NAACFetch(HTTPMethodView):
    @require_login()
    async def get(self, request: Request, jwt_data: JWT_Data, slug: str):
        executor = Mayim.get(NAACExecutor)

        methods = (
            method_name.replace("get_NAAC_", "")
            for method_name, _ in inspect.getmembers(
                executor, predicate=inspect.ismethod
            )
            if method_name.startswith("get_NAAC_")
        )

        if not slug:
            return json(
                {
                    method: {
                        "args": str(
                            inspect.signature(
                                getattr(NAACExecutor, f"get_NAAC_{method}")
                            )
                        )
                        .replace("self, ", "")
                        .replace("self", "")
                        .split(" -> ")[0],
                        "description": (
                            " ".join(
                                getattr(
                                    NAACExecutor, f"get_NAAC_{method}"
                                ).__doc__.split()
                            )
                            if getattr(NAACExecutor, f"get_NAAC_{method}").__doc__
                            else ""
                        ),
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
            method = getattr(NAACExecutor, f"get_NAAC_{slug}")
            call = getattr(executor, f"get_NAAC_{slug}")

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
            data: List[T] = await call(**args) if needs_args else await call()

            if not data:
                return json(
                    {
                        "data": [],
                        "description": (
                            " ".join(
                                getattr(
                                    NAACExecutor, f"get_NAAC_{slug}"
                                ).__doc__.split()
                            )
                            if getattr(NAACExecutor, f"get_NAAC_{slug}").__doc__
                            else ""
                        ),
                    }
                )
            return json(
                {
                    "data": [d.to_dict() for d in data],
                    "description": (
                        " ".join(
                            getattr(NAACExecutor, f"get_NAAC_{slug}").__doc__.split()
                        )
                        if getattr(NAACExecutor, f"get_NAAC_{slug}").__doc__
                        else ""
                    ),
                }
            )
        except Exception as e:
            ref_id = uuid.uuid4()
            logger.error(
                f"REF ID: {ref_id}\nAn error occurred while fetching NAAC data: {str(e)}",
                exc_info=e,
            )
            return json(
                {"error": "Internal Server Error", "reference_id": str(ref_id)}, 500
            )
