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
    sdg_goals: Optional[UUID] = None
