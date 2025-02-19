from pydantic import BaseModel
from uuid import UUID


class GPA(BaseModel):
    student_id: UUID
    semester: int
    GPA: float
    credits: int

    def to_dict(self):
        return {
            "student_id": str(self.student_id),
            "semester": self.semester,
            "GPA": self.GPA,
            "credits": self.credits,
        }
