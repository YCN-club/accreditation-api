from pydantic import BaseModel
from uuid import UUID, uuid4


class GPA(BaseModel):
    student_id: UUID = uuid4()
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
