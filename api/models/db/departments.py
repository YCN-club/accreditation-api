from pydantic import BaseModel
from uuid import UUID


class Departments(BaseModel):
    id: UUID
    name: str
    program_id: UUID
