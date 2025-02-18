from pydantic import BaseModel
from uuid import UUID


class ProgramIntakes(BaseModel):
    program_id: UUID
    year: int
    intake: int

    def to_dict(self):
        return {
            "program_id": str(self.program_id),
            "year": self.year,
            "intake": self.intake,
        }
