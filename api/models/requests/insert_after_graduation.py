from pydantic import BaseModel
from uuid import UUID

from api.models.enums import AfterGraduationType


class AfterGraduation(BaseModel):
    id: UUID
    student_id: UUID
    year: int
    type: AfterGraduationType

    def to_dict(self):
        return {
            "id": str(self.id),
            "student_id": str(self.student_id),
            "year": self.year,
            "type": self.type,
        }

