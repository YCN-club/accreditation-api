from pydantic import BaseModel
from uuid import UUID


class AfterGraduationHigherStudies(BaseModel):
    after_graduation_id: UUID
    institute_name: str
    program_name: str
    with_exam: bool = True
