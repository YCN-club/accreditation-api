from pydantic import BaseModel
from uuid import UUID, uuid4


class OtherAcademicInstitutesRunByTrustSociety(BaseModel):
    id: UUID = uuid4()
    name: str
    year_of_establishment: int
    program_of_study: list[str]
    location: str

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "year_of_establishment": self.year_of_establishment,
            "program_of_study": self.program_of_study,
            "location": self.location,
        }
