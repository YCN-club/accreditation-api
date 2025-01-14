from pydantic import BaseModel
from uuid import UUID


class GPA(BaseModel):
    student_id: UUID
    semester: int
    GPA: float
    credits: int
