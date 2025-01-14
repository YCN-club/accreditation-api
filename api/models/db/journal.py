from pydantic import BaseModel
from uuid import UUID

from api.models.enums import JournalFrequency, JournalPublicationType


class Journal(BaseModel):
    id: UUID
    name: str
    frequency: JournalFrequency
    type: JournalPublicationType
    scopus_indexed: bool
