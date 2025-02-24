from pydantic import BaseModel
from uuid import UUID, uuid4


class Departments(BaseModel):
    id: UUID = uuid4()
    name: str
    program_id: UUID = uuid4()

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "program_id": str(self.program_id),
        }
