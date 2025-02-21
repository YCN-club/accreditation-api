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

    def to_dict(self):
        return {
            "id": str(self.id),
            "institute_code": self.institute_code,
            "name": self.name,
            "type": self.type,
            "year_of_establishment": self.year_of_establishment,
            "ownership_status": self.ownership_status,
            "affiliating_university_name": self.affiliating_university_name,
            "affiliating_university_address": self.affiliating_university_address,
            "vision": self.vision,
            "mission": self.mission,
            "other_academic_institute_ids": [
                str(id) for id in self.other_academic_institute_ids
            ],
            "programs_offered": [str(id) for id in self.programs_offered],
            "programs_considered": [str(id) for id in self.programs_considered],
            "head_of_institute_id": str(self.head_of_institute_id),
            "nba_coordinator_id": str(self.nba_coordinator_id),
        }

