from pydantic import BaseModel
from uuid import UUID

from api.models.enums import NationalGovernmentExamType


class NationalGovernmentExams(BaseModel):
    id: UUID
    student_id: UUID
    exam_type: NationalGovernmentExamType
