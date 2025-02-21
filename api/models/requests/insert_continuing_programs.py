from pydantic import BaseModel
from uuid import UUID


class ContinuingEducationPrograms(BaseModel):
    id: UUID
    year: int
    name: str
    no_of_participants: int
    no_of_days: int

    def to_dict(self):
        return {
            "id": str(self.id),
            "year": self.year,
            "name": self.name,
            "no_of_participants": self.no_of_participants,
            "no_of_days": self.no_of_days,
        }

