from pydantic import BaseModel
from uuid import UUID


class ContinuingEducationPrograms(BaseModel):
    id: UUID
    year: int
    name: str
    no_of_participants: int
    no_of_days: int
