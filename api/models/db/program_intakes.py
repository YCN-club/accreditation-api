from pydantic import BaseModel
from uuid import UUID


class ProgramIntakes(BaseModel):
    program_id: UUID
    year: int
    intake: int
