from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class Auth(BaseModel):
    id: UUID
    password: str
    last_login: Optional[datetime] = None
    requires_reset: bool = False
