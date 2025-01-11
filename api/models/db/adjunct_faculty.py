from pydantic import BaseModel
from uuid import UUID


class AdjunctFaculty(BaseModel):
    faculty_id: UUID
    hours_handled: int
    subjects: list[str]
