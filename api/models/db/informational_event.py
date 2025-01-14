from pydantic import BaseModel
from uuid import UUID


class InformationalEvent(BaseModel):
    id: UUID
    speaker: str
    no_of_students: int
    no_of_teachers: int
