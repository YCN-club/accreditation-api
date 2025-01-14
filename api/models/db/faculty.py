from pydantic import BaseModel
from uuid import UUID
from datetime import date
from typing import Optional

from api.models.enums import (
    FacultyContractualObligation,
    FacultyHighestDegree,
    FacultyNatureOfAssociation,
)


class Faculty(BaseModel):
    id: UUID
    employee_id: Optional[str]
    department: Optional[str]
    employee_id: Optional[str]
    department: Optional[str]
    designation: str
    pan_no: str
    apaar_id: Optional[str]
    highest_degree: FacultyHighestDegree
    university: str
    area_of_specialization: str
    date_of_join: date
    designation_at_join: str
    designated_as_professor: Optional[date]
    designated_as_associate_professor: Optional[date]
    designated_as_assistant_professor: Optional[date]
    nature_of_association: FacultyNatureOfAssociation
    contractual_obligation: FacultyContractualObligation
    currently_associated: bool = True
    date_of_leave: Optional[date]
