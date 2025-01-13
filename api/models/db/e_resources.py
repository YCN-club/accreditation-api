from pydantic import BaseModel
from uuid import UUID


class EResources(BaseModel):
    faculty_id: UUID
    name: str
    development_platform: str
    date_of_launch: str
    link_to_relevant_document: str
    institute: str
