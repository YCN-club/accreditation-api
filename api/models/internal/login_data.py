from uuid import UUID

import bcrypt
from pydantic import BaseModel


class LoginData(BaseModel):
    user_id: UUID
    name: str
    email: str
    password: str
    is_active: bool
    requires_reset: bool

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def to_dict(self):
        return {
            "user_id": str(self.user_id),
            "name": self.name,
            "email": self.email,
        }
