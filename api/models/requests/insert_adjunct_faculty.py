from pydantic import BaseModel
from uuid import UUID, uuid4


class AdjunctFaculty(BaseModel):
    faculty_id: UUID = uuid4()
    hours_handled: int
    subjects: list[str]

    def to_dict(self):
        return {
            "faculty_id": str(self.faculty_id),
            "hours_handled": self.hours_handled,
            "subjects": self.subjects,
        }
