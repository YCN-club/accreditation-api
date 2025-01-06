from pydantic import BaseModel
from uuid import UUID

from api.models.enums import IprStatus, IprType


class Ipr(BaseModel):
    id: UUID
    year: int
    type: IprType
    status: IprStatus
