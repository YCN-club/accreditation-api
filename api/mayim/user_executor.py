from uuid import UUID
from mayim import PostgresExecutor

from api.models.db.user import User


class UserExecutor(PostgresExecutor):
    generic_prefix = ""
    path = "./queries/users/"

    async def check_if_user_can_login(self, email_id: str) -> bool:
        """
        Check if a user can login.
        """

    async def create_user_login(self, user_id: UUID, password_hash: str) -> None:
        """
        Create a new login in the database.
        """

    async def update_user_password(self, user_id: UUID, password_hash: str) -> None:
        """
        Update a user's password in the database.
        """

    async def get_user_by_email(self, email: str) -> User:
        """
        Get a user by their email.
        """
