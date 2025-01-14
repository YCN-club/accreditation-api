from pydantic import BaseModel
from uuid import UUID


class IprEarnings(BaseModel):
    id: UUID
    financial_year: int
    amount_inr: float
