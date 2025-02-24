from pydantic import BaseModel
from uuid import UUID, uuid4


class Awards(BaseModel):
    id: UUID = uuid4()
    name: str
    type: str
    awarding_agency: str
    user_type: str
    user_id: UUID = uuid4()
    year: int

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "type": self.type,
            "awarding_agency": self.awarding_agency,
            "user_type": self.user_type,
            "user_id": str(self.user_id),
            "year": self.year,
        }
