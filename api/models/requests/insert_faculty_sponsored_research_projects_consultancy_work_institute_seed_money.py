from pydantic import BaseModel
from uuid import UUID


class FacultySponsoredResearchProjectsConsultancyWorkInstituteSeedMoney(BaseModel):
    faculty_id: UUID
    name_of_principal_investigator: str
    name_of_co_principal_investigator: str
    department_id: UUID
    project_title: str
    name_of_funding_agency: str
    duration_of_project: str
    amount_inr: int
    outcomes: str

    def to_dict(self):
        return {
            "faculty_id": str(self.faculty_id),
            "name_of_principal_investigator": self.name_of_principal_investigator,
            "name_of_co_principal_investigator": self.name_of_co_principal_investigator,
            "department_id": str(self.department_id),
            "project_title": self.project_title,
            "name_of_funding_agency": self.name_of_funding_agency,
            "duration_of_project": self.duration_of_project,
            "amount_inr": self.amount_inr,
            "outcomes": self.outcomes,
        }
