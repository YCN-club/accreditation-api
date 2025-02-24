from pydantic import BaseModel
from uuid import UUID, uuid4

from api.models.enums import AcademicSemester, BookPublicationType


class BookPublication(BaseModel):
    id: UUID = uuid4()
    year: int
    semester: AcademicSemester
    title: str
    isbn: int
    type: BookPublicationType

    def to_dict(self):
        return {
            "id": str(self.id),
            "year": self.year,
            "semester": self.semester,
            "title": self.title,
            "isbn": self.isbn,
            "type": self.type,
        }
