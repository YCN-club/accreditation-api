from pydantic import BaseModel
from uuid import UUID, uuid4


class LaboratoriesTechnicalManpower(BaseModel):
    id: UUID = uuid4()
    name: str
    designation: str
    qualification: str

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "designation": self.designation,
            "qualification": self.qualification,
        }
