from pydantic import BaseModel
from uuid import UUID


class ProfessionalCommunities(BaseModel):
    faculty_id: UUID
    name_of_society: str
    position: str

    def to_dict(self):
        return {
            "faculty_id": str(self.faculty_id),
            "name_of_society": self.name_of_society,
            "position": self.position,
        }
