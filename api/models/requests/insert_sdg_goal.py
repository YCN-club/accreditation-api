from pydantic import BaseModel
from uuid import UUID


class SdgGoal(BaseModel):
    id: UUID
    number: int
    goal: str

    def to_dict(self):
        return {"id": str(self.id), "number": self.number, "goal": self.goal}

