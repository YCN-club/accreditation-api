from pydantic import BaseModel
from uuid import UUID


class Facilities(BaseModel):
    id: UUID
    name: str
    type: str
    is_ict: bool = False
    details: str = None
    reasons: list[str]
    utilization: str = None
    relevance_to_pos: str

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "type": self.type,
            "is_ict": self.is_ict,
            "details": self.details,
            "reasons": self.reasons,
            "utilization": self.utilization,
            "relevance_to_pos": self.relevance_to_pos,
        }
