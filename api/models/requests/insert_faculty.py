from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import date
from typing import Optional

from api.models.enums import (
    FacultyContractualObligation,
    FacultyHighestDegree,
    FacultyNatureOfAssociation,
)


class Faculty(BaseModel):
    id: UUID = uuid4()
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

    def to_dict(self):
        return {
            "id": str(self.id),
            "employee_id": self.employee_id,
            "department": self.department,
            "designation": self.designation,
            "pan_no": self.pan_no,
            "apaar_id": self.apaar_id,
            "highest_degree": self.highest_degree,
            "university": self.university,
            "area_of_specialization": self.area_of_specialization,
            "date_of_join": self.date_of_join,
            "designation_at_join": self.designation_at_join,
            "designated_as_professor": self.designated_as_professor,
            "designated_as_associate_professor": self.designated_as_associate_professor,
            "designated_as_assistant_professor": self.designated_as_assistant_professor,
            "nature_of_association": self.nature_of_association,
            "contractual_obligation": self.contractual_obligation,
            "currently_associated": self.currently_associated,
            "date_of_leave": self.date_of_leave,
        }
