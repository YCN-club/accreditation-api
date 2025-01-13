from pydantic import BaseModel
from uuid import UUID


class Awards(BaseModel):
    id: UUID
    name: str
    type: str
    awarding_agency: str
    user_type: str
    user_id: UUID
    year: int
