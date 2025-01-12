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
