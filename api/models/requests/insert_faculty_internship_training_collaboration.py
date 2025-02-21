from pydantic import BaseModel
from uuid import UUID


class FacultyInternshipTrainingCollaboration(BaseModel):
    faculty_id: UUID
    name_of_itc: str
    name_of_company: str
    type: str
    outcomes: str

    def to_dict(self):
        return {
            "faculty_id": str(self.faculty_id),
            "name_of_itc": self.name_of_itc,
            "name_of_company": self.name_of_company,
            "type": self.type,
            "outcomes": self.outcomes,
        }

