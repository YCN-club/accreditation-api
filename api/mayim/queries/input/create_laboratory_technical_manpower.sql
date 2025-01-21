CREATE TABLE "laboratory_technical_manpower" (
  "laboratory_id" uuid,
  "technical_manpower_id" uuid,
  PRIMARY KEY ("laboratory_id", "technical_manpower_id"),
  FOREIGN KEY ("laboratory_id") REFERENCES "laboratories" ("id"),
  FOREIGN KEY ("technical_manpower_id") REFERENCES "laboratories_technical_manpower" ("id")
);
