from pydantic import BaseModel
from uuid import UUID, uuid4


class AfterGraduationEntrepreneurship(BaseModel):
    after_graduation_id: UUID = uuid4()
    company_name: str

    def to_dict(self):
        return {
            "after_graduation_id": self.after_graduation_id,
            "company_name": self.company_name,
        }
