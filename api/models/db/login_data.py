from uuid import UUID

from pydantic import BaseModel


class LoginData(BaseModel):
    user_id: UUID
    employee_id: str
    password: str
    is_active: bool
    requires_reset: bool
