from pydantic import BaseModel
from uuid import UUID


class Companies(BaseModel):
    id: UUID
    name: str
    contact_no: str
    contact_email: str
