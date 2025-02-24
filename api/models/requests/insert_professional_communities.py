from uuid import UUID
from pydantic import BaseModel


class professional_communities(BaseModel):
    faculty_id: UUID
    name_of_society: str
    position: str
