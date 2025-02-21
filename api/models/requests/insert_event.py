from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from uuid import UUID

from api.models.enums import EventLevel, EventObjective


class Event(BaseModel):
    id: UUID
    name: str
    date: Optional[datetime] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    venue: str
    organizer_id: UUID
    level: Optional[EventLevel] = None
    objective: Optional[EventObjective] = None
    description: Optional[str] = None

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "date": self.date,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "venue": self.venue,
            "organizer_id": str(self.organizer_id),
            "level": self.level if self.level else None,
            "objective": self.objective if self.objective else None,
            "description": self.description,
        }
