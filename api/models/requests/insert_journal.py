from pydantic import BaseModel
from uuid import UUID, uuid4

from api.models.enums import JournalFrequency, JournalPublicationType


class Journal(BaseModel):
    id: UUID = uuid4()
    name: str
    frequency: JournalFrequency
    type: JournalPublicationType
    scopus_indexed: bool

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "frequency": self.frequency,
            "type": self.type,
            "scopus_indexed": self.scopus_indexed,
        }
