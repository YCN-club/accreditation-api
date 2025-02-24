from pydantic import BaseModel
from uuid import UUID, uuid4


class BookPublicationAuthor(BaseModel):
    publication_id: UUID = uuid4()
    author_id: UUID = uuid4()
    author_index: int

    def to_dict(self):
        return {
            "publication_id": str(self.publication_id),
            "author_id": str(self.author_id),
            "author_index": self.author_index,
        }
