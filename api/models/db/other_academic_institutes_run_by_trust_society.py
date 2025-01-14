from pydantic import BaseModel
from uuid import UUID


class OtherAcademicInstitutesRunByTrustSociety(BaseModel):
    id: UUID
    name: str
    year_of_establishment: int
    program_of_study: list[str]
    location: str
