from pydantic import BaseModel
from uuid import UUID, uuid4


class FacultyCourses(BaseModel):
    faculty_id: UUID = uuid4()
    name_of_course: str
    developed: bool = False

    def to_dict(self):
        return {
            "faculty_id": str(self.faculty_id),
            "name_of_course": self.name_of_course,
            "developed": self.developed,
        }
