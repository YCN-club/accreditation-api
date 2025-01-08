from pydantic import BaseModel
from uuid import UUID


class Institute(BaseModel):
    id: UUID
    institute_code: int
    name: str
