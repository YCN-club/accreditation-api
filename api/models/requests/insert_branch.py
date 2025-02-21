from pydantic import BaseModel
from uuid import UUID


class Branches(BaseModel):
    id: UUID
    name: str
    department_id: UUID

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "department_id": self.department_id,
        }

