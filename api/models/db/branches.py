from pydantic import BaseModel
from uuid import UUID


class Branches(BaseModel):
    id: UUID
    name: str
    department_id: UUID
