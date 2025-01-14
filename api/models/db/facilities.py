from pydantic import BaseModel
from uuid import UUID


class Facilities(BaseModel):
    id: UUID
    name: str
    type: str
    is_ict: bool = False
    details: str = None
    reasons: list[str]
    utilization: str = None
    relevance_to_pos: str
