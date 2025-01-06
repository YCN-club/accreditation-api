from pydantic import BaseModel
from typing import Optional
from uuid import UUID

from api.models.enums import SocialDisadvantage


class Student(BaseModel):
    id: UUID
    admission_no: str
    registration_no: str
    program_id: UUID
    year_of_join: int
    social_disadvantage: Optional[SocialDisadvantage] = None
    economic_disadvantage: bool = False
    physically_challenged: bool = False
