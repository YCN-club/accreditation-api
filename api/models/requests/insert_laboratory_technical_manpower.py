from uuid import UUID
from pydantic import BaseModel


class laboratory_technical_manpower(BaseModel):
    laboratory_id: UUID
    technical_manpower_id: UUID

    def to_dict(self):
        return {
            "laboratory_id": str(self.laboratory_id),
            "technical_manpower_id": str(self.technical_manpower_id),
        }
