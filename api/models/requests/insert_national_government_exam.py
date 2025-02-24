from pydantic import BaseModel
from uuid import UUID, uuid4

from api.models.enums import NationalGovernmentExamType


class NationalGovernmentExams(BaseModel):
    id: UUID = uuid4()
    student_id: UUID = uuid4()
    exam_type: NationalGovernmentExamType

    def to_dict(self):
        return {
            "id": str(self.id),
            "student_id": str(self.student_id),
            "exam_type": self.exam_type,
        }
