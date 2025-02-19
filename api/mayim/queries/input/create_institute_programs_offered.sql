CREATE TABLE "institute_programs_offered" (
  "institute_id" uuid,
  "program_id" uuid,
  PRIMARY KEY ("institute_id", "program_id"),
  FOREIGN KEY ("institute_id") REFERENCES "institutes" ("id"),
  FOREIGN KEY ("program_id") REFERENCES "programs" ("id")
);
