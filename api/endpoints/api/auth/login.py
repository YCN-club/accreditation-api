from mayim import Mayim
from sanic import Request, json
from sanic.views import HTTPMethodView
from sanic_ext import validate

from api.app import API

from api.mayim.auth_executor import AuthExecutor
from api.models.requests.login_json import LoginJSON


class AuthLogin(HTTPMethodView):

    @validate(json=LoginJSON, body_argument="data")
    async def post(self, request: Request, data: LoginJSON):
        # Get the executor
        executor = Mayim.get(AuthExecutor)

        app: API = request.app

        # Get the username and password from the request.
        username = data.username
        password = data.password

        # Get the user from the database.
        user = await executor.get_user_by_emp_id(username)

        # Check if the user exists.
        if user=={"error": "invalid_username"}:
            return json({"error": "invalid_username"}, status=401)

        # Check if the user is active.
        if not user.is_active:
            return json({"error": "inactive_user"}, status=401)

        # Check if the password is correct.
        authenticated = user.check_password(password)

        # Check if the user is authenticated.
        if not authenticated:
            return json({"error": "invalid_password"}, status=401)

        # Check if password reset is required.
        if user.requires_reset:
            #  Generate a token and return it.
            data = {
                "name": user.employee_id,
                "email": user.email,
                "roles": ["password_reset"],
                "uuid": user.user_id,
            }
            token = await app.generate_jwt(data=data, validity=30)
            return json(
                {"message": "password_reset_required", "token": token}, status=200
            )

        # Generate a JWT token.
        # TODO: Add roles to the user.
        data = {
            "name": user.employee_id,
            "email": user.email,
            "roles": [],
            "uuid": user.user_id,
        }
        token = await app.generate_jwt(user)
        # Return Token.
        return json({"token": token, "message": "Authenticated"}, status=200)
