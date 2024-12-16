from mayim import Mayim
from sanic import Request, json
from sanic.views import HTTPMethodView
from sanic_ext import validate
import bcrypt
import uuid

from api.app import API

from api.mayim.auth_executor import AuthExecutor
from api.models.db.login_data import LoginData

class AuthSignUp(HTTPMethodView):

    @validate(json=LoginData, body_argument="data")
    async def post(self, request: Request, data: LoginData):
        """
        Sign up a new user.
        """
        # Get the executor
        executor = Mayim.get(AuthExecutor)

        app: API = request.app

        # Get the username from the request.
        username = data.employee_id

        # Get the user from the database.
        user = await executor.get_user_by_emp_id(username)

        # Check if the user exists.
        if user=={"error": "invalid_username"}:
            pass
        else:
            return json({"error": "username_exists"}, status=401)
        
        # Get the password from the request.
        password = data.password

        # Hash the password.
        password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

        # Insert the user into the database.
        user = LoginData(
            user_id=uuid.uuid4(),
            name=data.name,
            email=data.email,
            employee_id=data.employee_id,
            password=password_hash,
            is_active=True,
            requires_reset=False
        )

        await executor.insert_user(user)

        return json({"message": "user_created"}, status=200)

