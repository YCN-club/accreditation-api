from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4

from api.models.enums import AcademicSemester


class JournalPublication(BaseModel):
    id: UUID = uuid4()
    journal_id: UUID = uuid4()
    journal_volume_number: int
    journal_issue_number: int
    sponsor_id: Optional[UUID] = None
    year: int
    semester: AcademicSemester
    doi: Optional[str] = None
    title: str

    def to_dict(self):
        return {
            "id": str(self.id),
            "journal_id": str(self.journal_id),
            "journal_volume_number": self.journal_volume_number,
            "journal_issue_number": self.journal_issue_number,
            "sponsor_id": str(self.sponsor_id) if self.sponsor_id else None,
            "year": self.year,
            "semester": self.semester,
            "doi": self.doi,
            "title": self.title,
        }
