from pydantic import BaseModel
from uuid import UUID


class Sponsorship(BaseModel):
    id: UUID
    agency_name: str
    year: int
    amount_inr: float
    project_title: str
