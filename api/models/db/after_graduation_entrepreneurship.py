from pydantic import BaseModel
from uuid import UUID


class AfterGraduationEntrepreneurship(BaseModel):
    after_graduation_id: UUID
    company_name: str
