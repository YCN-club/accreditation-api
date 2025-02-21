from uuid import UUID

import bcrypt
from pydantic import BaseModel


class LoginData(BaseModel):
    uuid: UUID
    name: str
    email: str
    password: str
    is_active: bool
    requires_reset: bool
    roles: list[str] = []

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def to_dict(self):
        return {
            "uuid": str(self.uuid),
            "name": self.name,
            "email": self.email,
            "roles": self.roles,
        }
