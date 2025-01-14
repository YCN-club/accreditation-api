from pydantic import BaseModel
from uuid import UUID


class LaboratoriesTechnicalManpower(BaseModel):
    id: UUID
    name: str
    designation: str
    qualification: str
