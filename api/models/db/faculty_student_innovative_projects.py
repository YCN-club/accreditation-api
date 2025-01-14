from pydantic import BaseModel
from uuid import UUID


class FacultyStudentInnovativeProjects(BaseModel):
    faculty_id: UUID
    name_of_event: str
    link_of_website: str
