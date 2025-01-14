from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class User(BaseModel):
    id: UUID
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    email: str
