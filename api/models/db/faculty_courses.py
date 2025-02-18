from pydantic import BaseModel
from uuid import UUID


class FacultyCourses(BaseModel):
    faculty_id: UUID
    name_of_course: str
    developed: bool = False

    def to_dict(self):
        return {
            "faculty_id": str(self.faculty_id),
            "name_of_course": self.name_of_course,
            "developed": self.developed,
        }
