from pydantic import BaseModel
from uuid import UUID


class Program(BaseModel):
    id: UUID
    program_code: int
    institute_id: UUID
    duration_year: int
    name: str
