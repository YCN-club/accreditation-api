from pydantic import BaseModel
from uuid import UUID

from api.models.enums import InstituteOwnershipStatus, InstituteType


class Institute(BaseModel):
    id: UUID
    institute_code: int
    name: str
    type: InstituteType
    year_of_establishment: int
    ownership_status: InstituteOwnershipStatus
    affiliating_university_name: str
    affiliating_university_address: str
    vision: str
    mission: str
    other_academic_institute_ids: list[UUID]
    programs_offered: list[UUID]
    programs_considered: list[UUID]
    head_of_institute_id: UUID
    nba_coordinator_id: UUID
