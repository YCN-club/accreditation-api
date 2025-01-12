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
