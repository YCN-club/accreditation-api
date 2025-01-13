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
    link_to_relevant_documents: str
