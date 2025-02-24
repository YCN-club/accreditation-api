from pydantic import BaseModel
from uuid import UUID, uuid4

from api.models.enums import CollaborativeActivityType


class CollaborativeActivity(BaseModel):
    id: UUID = uuid4()
    title: str
    type: CollaborativeActivityType
    agency_id: UUID = uuid4()
    user_id: UUID = uuid4()
    source_of_financial_support: str
    year: int
    duration: int
    link_to_relevant_documents: str

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
