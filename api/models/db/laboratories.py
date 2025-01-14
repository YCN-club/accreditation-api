from pydantic import BaseModel
from uuid import UUID


class Laboratories(BaseModel):
    id: UUID
    batch_size: int
    name_of_equipment: list[str]
    safety_measures: list[str]
    weekly_utilization: int
    technical_manpower_ids: list[UUID]
