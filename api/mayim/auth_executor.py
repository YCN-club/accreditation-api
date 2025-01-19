from mayim import PostgresExecutor

from api.models.internal.login_data import LoginData


class AuthExecutor(PostgresExecutor):
    generic_prefix = ""
    path = "./queries/auth/"

    async def get_login_by_email(self, email: str) -> LoginData:
        """
        Get LoginData by email.
        """
