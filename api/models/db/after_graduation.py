from pydantic import BaseModel
from uuid import UUID

from api.models.enums import AfterGraduationType


class AfterGraduation(BaseModel):
    id: UUID
    student_id: UUID
    year: int
    type: AfterGraduationType
