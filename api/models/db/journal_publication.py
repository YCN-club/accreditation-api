from pydantic import BaseModel
from typing import Optional
from uuid import UUID

from api.models.enums import AcademicSemester


class JournalPublication(BaseModel):
    id: UUID
    journal_id: UUID
    journal_volume_number: int
    journal_issue_number: int
    sponsor_id: Optional[UUID] = None
    year: int
    semester: AcademicSemester
    doi: Optional[str] = None
    title: str
