from pydantic import BaseModel
from uuid import UUID


class AfterGraduationPlacements(BaseModel):
    after_graduation_id: UUID
    employer_id: UUID
    salary: int
