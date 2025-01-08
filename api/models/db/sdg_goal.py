from pydantic import BaseModel
from uuid import UUID


class SdgGoal(BaseModel):
    id: UUID
    number: int
    goal: str
