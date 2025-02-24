from pydantic import BaseModel
from uuid import UUID, uuid4

from api.models.enums import BenefitSchemeType


class BenefitPrograms(BaseModel):
    id: UUID = uuid4()
    student_id: UUID = uuid4()
    year: int
    type: BenefitSchemeType

    def to_dict(self):
        return {
            "id": str(self.id),
            "student_id": str(self.student_id),
            "year": self.year,
            "type": self.type,
        }
