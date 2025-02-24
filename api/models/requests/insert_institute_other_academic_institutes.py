from uuid import UUID
from pydantic import BaseModel


class institute_other_academic_institutes(BaseModel):
    institute_id: UUID
    other_academic_institute_id: UUID

    def to_dict(self):
        return {
            "institute_id": str(self.institute_id),
            "other_academic_institute_id": str(self.other_academic_institute_id),
        }
