from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4


class User(BaseModel):
    id: UUID = uuid4()
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    email: str

    def to_dict(self):
        return {
            "id": str(self.id),
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
            "email": self.email,
        }
