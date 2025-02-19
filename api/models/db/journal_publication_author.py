from pydantic import BaseModel
from uuid import UUID


class JournalPublicationAuthor(BaseModel):
    publication_id: UUID
    author_id: UUID
    author_index: int

    def to_dict(self):
        return {
            "publication_id": str(self.publication_id),
            "author_id": str(self.author_id),
            "author_index": self.author_index,
        }
