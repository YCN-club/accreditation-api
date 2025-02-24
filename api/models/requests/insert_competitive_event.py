from pydantic import BaseModel
from uuid import UUID, uuid4

from api.models.enums import CompetitiveEventType, EventClassification


class CompetitiveEvent(BaseModel):
    id: UUID = uuid4()
    classification: EventClassification
    participant_id: UUID = uuid4()
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
