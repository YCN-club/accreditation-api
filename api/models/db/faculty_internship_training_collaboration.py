from pydantic import BaseModel
from uuid import UUID


class FacultyInternshipTrainingCollaboration(BaseModel):
    faculty_id: UUID
    name_of_itc: str
    name_of_company: str
    type: str
    outcomes: str
