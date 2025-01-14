from pydantic import BaseModel
from uuid import UUID


class ProfessionalCommunities(BaseModel):
    faculty_id: UUID
    name_of_society: str
    position: str
