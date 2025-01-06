from pydantic import BaseModel
from uuid import UUID


class Faculty(BaseModel):
    id: UUID
    employee_id: str
    department: str
    designation: str
