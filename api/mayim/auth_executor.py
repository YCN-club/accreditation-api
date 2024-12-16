from mayim import PostgresExecutor

from api.models.db.login_data import LoginData


class AuthExecutor(PostgresExecutor):
    generic_prefix = ""
    path = "./queries/auth/"

    async def get_user_by_emp_id(self, employee_id: str) -> LoginData:
        """
        Get a user from the database by their employee ID.
        This method maps the database row to the LoginData model.
        """
        query = """
        SELECT 
            user_id, 
            name, 
            email, 
            employee_id, 
            password AS hashed_password, 
            is_active, 
            requires_reset 
        FROM login_data 
        WHERE employee_id = $1
        """
        
        row = await self.run_sql(query=query, as_list=False, posargs=(employee_id,))

        if not row:
            return {"error": "invalid_username"}

        return LoginData(**row)


    async def update_user_password(self, username: str, password_hash: str) -> None:
        """
        Update a user's password in the database.
        """
        query = """
        UPDATE users
        SET password = $2
        WHERE employee_id = $1
        """
        await self.execute(query, username, password_hash)
