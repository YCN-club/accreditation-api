from pydantic import BaseModel
from uuid import UUID


class IprEarnings(BaseModel):
    id: UUID
    financial_year: int
    amount_inr: float

    def to_dict(self):
        return {
            "id": str(self.id),
            "financial_year": self.financial_year,
            "amount_inr": self.amount_inr,
        }

