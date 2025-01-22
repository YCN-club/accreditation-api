from mayim import Mayim
from sanic import Request, json
from sanic.views import HTTPMethodView
from sanic.log import logger
from sanic_ext import validate
import bcrypt
import uuid

from api.mayim.user_executor import UserExecutor
from api.models.requests.auth.register_post import RegisterPost


class AuthRegister(HTTPMethodView):

    @validate(form=RegisterPost, body_argument="data")
    async def post(self, request: Request, data: RegisterPost):
        """
        Creates the auth entry for a user
        """
        # Get the executor
        user_executor = Mayim.get(UserExecutor)

        # Get the username from the request.
        username = data.email

        # Check if the user already exists
        try:
            exists = await user_executor.check_if_user_can_login(username)
        except Exception as e:
            logger.error(e)
            return json({"error": "internal_server_error"}, status=500)

        if exists:
            return json({"error": "user_exists"}, status=400)
        else:
            user = await user_executor.get_user_by_email(username)
            # Generate a random password
            password = str(uuid.uuid4())
            password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

            # Create the user
            try:
                await user_executor.create_user_login(user.id, password_hash)
            except Exception as e:
                logger.error(e)
                return json({"error": "internal_server_error"}, status=500)

            # Return the password
            return json({"password": password}, status=200)
