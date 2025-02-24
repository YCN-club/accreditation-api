from pydantic import BaseModel
from uuid import UUID, uuid4


class AfterGraduationPlacements(BaseModel):
    after_graduation_id: UUID = uuid4()
    employer_id: UUID = uuid4()
    salary: int

    def to_dict(self):
        return {
            "after_graduation_id": str(self.after_graduation_id),
            "employer_id": str(self.employer_id),
            "salary": self.salary,
        }
