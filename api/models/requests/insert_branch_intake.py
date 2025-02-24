from pydantic import BaseModel
from uuid import UUID, uuid4


class BranchIntake(BaseModel):
    branch_id: UUID = uuid4()
    year: int
    allowed_batch_size: int

    def to_dict(self):
        return {
            "branch_id": str(self.branch_id),
            "year": self.year,
            "allowed_batch_size": self.allowed_batch_size,
        }
