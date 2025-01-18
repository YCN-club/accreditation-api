from mayim import PostgresExecutor

from api.models.internal.login_data import LoginData


class AuthExecutor(PostgresExecutor):
    generic_prefix = ""
    path = "./queries/auth/"

    async def get_login_by_emp_id(self, employee_id: str) -> LoginData:
        """
        Get LoginData by email.
        """
