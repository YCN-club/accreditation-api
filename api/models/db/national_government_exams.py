from pydantic import BaseModel
from uuid import UUID

from api.models.enums import NationalGovernmentExamType


class NationalGovernmentExams(BaseModel):
    id: UUID
    student_id: UUID
    exam_type: NationalGovernmentExamType

    def to_dict(self):
        return {
            "id": str(self.id),
            "student_id": str(self.student_id),
            "exam_type": self.exam_type,
        }
