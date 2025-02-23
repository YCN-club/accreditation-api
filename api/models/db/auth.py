from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class Auth(BaseModel):
    id: UUID
    password: str
    last_login: Optional[datetime] = None
    requires_reset: bool = False
    is_active: bool

    def to_dict(self):
        return {
            "id": str(self.id),
            "last_login": (
                self.last_login.strftime("%Y-%m-%d %H:%M:%S")
                if self.last_login
                else None
            ),
            "requires_reset": self.requires_reset,
            "is_active": self.is_active,
        }
