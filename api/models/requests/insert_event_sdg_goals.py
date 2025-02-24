from uuid import UUID
from pydantic import BaseModel


class event_sdg_goals(BaseModel):
    event_id: UUID
    sdg_goal_id: UUID

    def to_dict(self):
        return {"event_id": str(self.event_id), "sdg_goal_id": str(self.sdg_goal_id)}
