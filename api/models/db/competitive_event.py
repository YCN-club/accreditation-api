from pydantic import BaseModel
from uuid import UUID

from api.models.enums import CompetitiveEventType, EventClassification


class CompetitiveEvent(BaseModel):
    id: UUID
    classification: EventClassification
    participant_id: UUID
    position: int
    award: str
    type: CompetitiveEventType
