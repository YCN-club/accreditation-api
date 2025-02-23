from pydantic import BaseModel
from uuid import UUID

from api.models.enums import CollaborativeActivityType


class CollaborativeActivity(BaseModel):
    id: UUID
    title: str
    type: CollaborativeActivityType
    agency_id: UUID
    user_id: UUID
    source_of_financial_support: str
    year: int
    duration: int
    link_to_relevant_documents: list[str]

    def to_dict(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "type": self.type,
            "agency_id": str(self.agency_id),
            "user_id": str(self.user_id),
            "source_of_financial_support": self.source_of_financial_support,
            "year": self.year,
            "duration": self.duration,
            "link_to_relevant_documents": self.link_to_relevant_documents,
        }
