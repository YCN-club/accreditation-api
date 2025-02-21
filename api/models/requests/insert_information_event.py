from pydantic import BaseModel
from uuid import UUID


class InformationalEvent(BaseModel):
    id: UUID
    speaker: str
    no_of_students: int
    no_of_teachers: int

    def to_dict(self):
        return {
            "id": str(self.id),
            "speaker": self.speaker,
            "no_of_students": self.no_of_students,
            "no_of_teachers": self.no_of_teachers,
        }
