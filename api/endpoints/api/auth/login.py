from mayim import Mayim
from sanic import Request, json
from sanic.views import HTTPMethodView
from sanic.log import logger
from sanic_ext import validate
from mayim.exception import RecordNotFound
from api.app import API

from api.mayim.auth_executor import AuthExecutor
from api.models.requests.auth.login_post import LoginPost


class AuthLogin(HTTPMethodView):

    @validate(form=LoginPost, body_argument="data")
    async def post(self, request: Request, data: LoginPost):
        """
        Authenticate a user.
        """
        # Get the executor
        executor = Mayim.get(AuthExecutor)

        app: API = request.app

        # Get the username and password from the request.
        username = data.username
        password = data.password

        # Get the user from the database.
        try:
            user = await executor.get_login_by_emp_id(username)
        except RecordNotFound:
            return json({"error": "invalid_username"}, status=401)
        except Exception as e:
            logger.error(e)
            return json({"error": "internal_server_error"}, status=500)

        # Check if the user is active.
        if not user.is_active:
            return json({"error": "inactive_user"}, status=401)

        # Check if the user is authenticated.
        if not user.check_password(password):
            return json({"error": "invalid_password"}, status=401)

        # Check if password reset is required.
        if user.requires_reset:
            #  Generate a token and return it.
            data = {
                "name": user.name,
                "email": user.email,
                "roles": ["password_reset"],
                "uuid": str(user.user_id),
            }
            token = await app.generate_jwt(data=data, validity=30)
            return json(
                {"message": "password_reset_required", "token": token}, status=200
            )

        # Generate a JWT token.
        # TODO: Add roles to the user.
        data = {
            "name": user.name,
            "email": user.email,
            "roles": [],
            "uuid": str(user.user_id),
        }
        token = await app.generate_jwt(user)
        # Return Token.
        return json({"token": token, "message": "Authenticated"}, status=200)
