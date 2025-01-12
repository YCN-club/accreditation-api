from pydantic import BaseModel
from uuid import UUID


class BranchIntake(BaseModel):
    branch_id: UUID
    year: int
    allowed_batch_size: int
