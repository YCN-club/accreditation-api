from pydantic import BaseModel
from uuid import UUID


class JournalPublicationAuthor(BaseModel):
    publication_id: UUID
    author_id: UUID
    author_index: int
