from pydantic import BaseModel
from uuid import UUID

from api.models.enums import IprStatus, IprType


class Ipr(BaseModel):
    id: UUID
    awardee_id: UUID | None
    awarder_name: str | None
    government_recognized: bool = False
    year: int
    uuid: str
    title: str
    type: IprType
    status: IprStatus

    def to_dict(self):
        return {
            "id": str(self.id),
            "awardee_id": str(self.awardee_id),
            "awarder_name": self.awarder_name,
            "government_recognized": self.government_recognized,
            "year": self.year,
            "uuid": self.uuid,
            "title": self.title,
            "type": self.type,
            "status": self.status,
        }

