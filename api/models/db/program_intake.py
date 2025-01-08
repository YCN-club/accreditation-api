from pydantic import BaseModel
from uuid import UUID


class ProgramIntake(BaseModel):
    program_id: UUID
    year: int
    allowed_batch_size: int
