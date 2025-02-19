from pydantic import BaseModel
from uuid import UUID


class AfterGraduationEntrepreneurship(BaseModel):
    after_graduation_id: UUID
    company_name: str

    def to_dict(self):
        return {
            "after_graduation_id": self.after_graduation_id,
            "company_name": self.company_name,
        }
