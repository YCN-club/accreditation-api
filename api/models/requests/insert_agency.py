from pydantic import BaseModel
from uuid import UUID, uuid4


class Agencies(BaseModel):
    id: UUID = uuid4()
    name: str
    contact_no: str
    contact_email: str

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "contact_no": self.contact_no,
            "contact_email": self.contact_email,
        }
