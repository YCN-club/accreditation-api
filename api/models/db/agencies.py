from pydantic import BaseModel
from uuid import UUID


class Agencies(BaseModel):
    id: UUID
    name: str
    contact_no: str
    contact_email: str
