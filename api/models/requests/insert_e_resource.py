from pydantic import BaseModel
from uuid import UUID, uuid4


class EResources(BaseModel):
    faculty_id: UUID = uuid4()
    name: str
    development_platform: str
    date_of_launch: str
    link_to_relevant_document: str
    institute: str

    def to_dict(self):
        return {
            "faculty_id": str(self.faculty_id),
            "name": self.name,
            "development_platform": self.development_platform,
            "date_of_launch": self.date_of_launch,
            "link_to_relevant_document": self.link_to_relevant_document,
            "institute": self.institute,
        }
