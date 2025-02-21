from pydantic import BaseModel
from uuid import UUID

from api.models.enums import ProgramAccreditationStatus


class Program(BaseModel):
    id: UUID
    program_code: int
    duration_year: int
    name: str
    year_of_start: int
    sanctioned_intake: int
    aicte_approval_details: str
    accreditation_status: ProgramAccreditationStatus
    number_of_times_accredited: int
    institute_id: UUID

    def to_dict(self):
        return {
            "id": str(self.id),
            "program_code": self.program_code,
            "duration_year": self.duration_year,
            "name": self.name,
            "year_of_start": self.year_of_start,
            "sanctioned_intake": self.sanctioned_intake,
            "aicte_approval_details": self.aicte_approval_details,
            "accreditation_status": self.accreditation_status,
            "number_of_times_accredited": self.number_of_times_accredited,
            "institute_id": str(self.institute_id),
        }
