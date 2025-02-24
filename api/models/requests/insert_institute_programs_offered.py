from uuid import UUID
from pydantic import BaseModel


class institute_programs_offered(BaseModel):
    institute_id: UUID
    program_id: UUID

    def to_dict(self):
        return {
            "institute_id": str(self.institute_id),
            "program_id": str(self.program_id),
        }
