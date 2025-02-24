from pydantic import BaseModel
from uuid import UUID, uuid4


class SdgGoal(BaseModel):
    id: UUID = uuid4()
    number: int
    goal: str

    def to_dict(self):
        return {"id": str(self.id), "number": self.number, "goal": self.goal}
