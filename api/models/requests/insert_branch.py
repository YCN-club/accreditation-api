from pydantic import BaseModel
from uuid import UUID, uuid4


class Branches(BaseModel):
    id: UUID = uuid4()
    name: str
    department_id: UUID = uuid4()

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "department_id": self.department_id,
        }
