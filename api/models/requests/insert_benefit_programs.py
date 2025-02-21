from pydantic import BaseModel
from uuid import UUID

from api.models.enums import BenefitSchemeType


class BenefitPrograms(BaseModel):
    id: UUID
    student_id: UUID
    year: int
    type: BenefitSchemeType

    def to_dict(self):
        return {
            "id": str(self.id),
            "student_id": str(self.student_id),
            "year": self.year,
            "type": self.type,
        }
