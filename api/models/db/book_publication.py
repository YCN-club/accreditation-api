from pydantic import BaseModel
from uuid import UUID

from api.models.enums import AcademicSemester, BookPublicationType


class BookPublication(BaseModel):
    id: UUID
    year: int
    semester: AcademicSemester
    title: str
    isbn: int
    type: BookPublicationType
