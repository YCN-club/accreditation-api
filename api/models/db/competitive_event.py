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

    def to_dict(self):
        return {
            "id": str(self.id),
            "classification": self.classification,
            "participant_id": str(self.participant_id),
            "position": self.position,
            "award": self.award,
            "type": self.type,
        }
