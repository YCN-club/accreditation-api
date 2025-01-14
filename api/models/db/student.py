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
