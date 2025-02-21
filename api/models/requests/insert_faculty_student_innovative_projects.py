from pydantic import BaseModel
from uuid import UUID


class FacultyStudentInnovativeProjects(BaseModel):
    faculty_id: UUID
    name_of_event: str
    link_of_website: str

    def to_dict(self):
        return {
            "faculty_id": str(self.faculty_id),
            "name_of_event": self.name_of_event,
            "link_of_website": self.link_of_website,
        }

