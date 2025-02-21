from pydantic import BaseModel
from uuid import UUID


class Departments(BaseModel):
    id: UUID
    name: str
    program_id: UUID

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "program_id": str(self.program_id),
        }

