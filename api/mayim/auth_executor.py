from mayim import PostgresExecutor

from api.models.db.login_data import LoginData


class AuthExecutor(PostgresExecutor):
    generic_prefix = ""
    path = "./queries/auth/"

    async def get_user_by_emp_id(self, username: str) -> LoginData:
        """Get a user from the database."""

    async def update_user_password(self, username: str, password_hash: str) -> None:
        """Update the password of a user in the database."""
