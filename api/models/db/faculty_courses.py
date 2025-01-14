from pydantic import BaseModel
from uuid import UUID


class FacultyCourses(BaseModel):
    faculty_id: UUID
    name_of_course: str
    developed: bool = False
