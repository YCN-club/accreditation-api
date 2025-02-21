from pydantic import BaseModel
from uuid import UUID


class Sponsorship(BaseModel):
    id: UUID
    agency_name: str
    year: int
    amount_inr: float
    project_title: str

    def to_dict(self):
        return {
            "id": str(self.id),
            "agency_name": self.agency_name,
            "year": self.year,
            "amount_inr": self.amount_inr,
            "project_title": self.project_title,
        }
