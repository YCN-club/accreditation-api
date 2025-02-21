from pydantic import BaseModel
from typing import Optional
from uuid import UUID

from api.models.enums import SocialDisadvantage, StudentEntries, StudentExits


class Student(BaseModel):
    id: UUID
    admission_no: str
    registration_no: str
    origin: str
    gender: str
    branch_id: UUID
    batch_year: int
    origin: str
    gender: str
    branch_id: UUID
    batch_year: int
    year_of_join: int
    type_of_join: StudentEntries
    year_of_exit: Optional[int] = None
    type_of_exit: Optional[StudentExits] = None
    type_of_join: StudentEntries
    year_of_exit: Optional[int] = None
    type_of_exit: Optional[StudentExits] = None
    social_disadvantage: Optional[SocialDisadvantage] = None
    economic_disadvantage: bool = False
    physically_challenged: bool = False

    def to_dict(self):
        return {
            "id": str(self.id),
            "admission_no": self.admission_no,
            "registration_no": self.registration_no,
            "origin": self.origin,
            "gender": self.gender,
            "branch_id": str(self.branch_id),
            "batch_year": self.batch_year,
            "year_of_join": self.year_of_join,
            "type_of_join": self.type_of_join,
            "year_of_exit": self.year_of_exit,
            "type_of_exit": self.type_of_exit if self.type_of_exit else None,
            "social_disadvantage": (
                self.social_disadvantage if self.social_disadvantage else None
            ),
            "economic_disadvantage": self.economic_disadvantage,
            "physically_challenged": self.physically_challenged,
        }
