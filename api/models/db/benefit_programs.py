from pydantic import BaseModel
from uuid import UUID

from api.models.enums import BenefitSchemeType


class BenefitPrograms(BaseModel):
    id: UUID
    student_id: UUID
    year: int
    type: BenefitSchemeType
