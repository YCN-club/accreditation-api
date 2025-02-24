from pydantic import BaseModel
from uuid import UUID, uuid4


class ProgramIntakes(BaseModel):
    program_id: UUID = uuid4()
    year: int
    intake: int

    def to_dict(self):
        return {
            "program_id": str(self.program_id),
            "year": self.year,
            "intake": self.intake,
        }
