from pydantic import BaseModel
from uuid import UUID, uuid4

from api.models.enums import CommunityType


class Organizer(BaseModel):
    id: UUID = uuid4()
    type: CommunityType
    name: str

    def to_dict(self):
        return {"id": str(self.id), "type": self.type, "name": self.name}
