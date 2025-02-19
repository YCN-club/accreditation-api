CREATE TABLE "event_sdg_goals" (
  "event_id" uuid,
  "sdg_goal_id" uuid,
  PRIMARY KEY ("event_id", "sdg_goal_id"),
  FOREIGN KEY ("event_id") REFERENCES "events" ("id"),
  FOREIGN KEY ("sdg_goal_id") REFERENCES "sdg_goals" ("id")
);
