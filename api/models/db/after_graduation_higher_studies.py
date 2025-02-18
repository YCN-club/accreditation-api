from pydantic import BaseModel
from uuid import UUID


class AfterGraduationHigherStudies(BaseModel):
    after_graduation_id: UUID
    institute_name: str
    program_name: str
    with_exam: bool = True

    def to_dict(self):
        return {
            "after_graduation_id": str(self.after_graduation_id),
            "institute_name": self.institute_name,
            "program_name": self.program_name,
            "with_exam": self.with_exam,
        }
