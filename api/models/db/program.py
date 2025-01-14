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
