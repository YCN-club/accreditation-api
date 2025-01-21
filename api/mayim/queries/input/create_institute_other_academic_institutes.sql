CREATE TABLE "institute_other_academic_institutes" (
  "institute_id" uuid,
  "other_academic_institute_id" uuid,
  PRIMARY KEY ("institute_id", "other_academic_institute_id"),
  FOREIGN KEY ("institute_id") REFERENCES "institutes" ("id"),
  FOREIGN KEY ("other_academic_institute_id") REFERENCES "other_academic_institutes_run_by_trust_society" ("id")
);
