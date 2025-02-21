from pydantic import BaseModel
from uuid import UUID


class AfterGraduationPlacements(BaseModel):
    after_graduation_id: UUID
    employer_id: UUID
    salary: int

    def to_dict(self):
        return {
            "after_graduation_id": str(self.after_graduation_id),
            "employer_id": str(self.employer_id),
            "salary": self.salary,
        }
