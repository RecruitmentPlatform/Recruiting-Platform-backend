BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "company" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "employment_type" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "job_category" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "job_position" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "process" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL,
	"description"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "recruiter" (
	"id"	INTEGER NOT NULL UNIQUE,
	"company_id"	INTEGER,
	"first_name"	TEXT,
	"last_name"	TEXT,
	"email"	TEXT NOT NULL UNIQUE,
	"phone"	TEXT,
	"description"	TEXT,
	"pass_hash"	TEXT NOT NULL,
	"session_id"	INTEGER,
	FOREIGN KEY("company_id") REFERENCES "company"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "experience" (
	"id"	INTEGER NOT NULL UNIQUE,
	"candidate_id"	INTEGER NOT NULL,
	"company_id"	INTEGER NOT NULL,
	"date_start"	INTEGER,
	"date_end"	INTEGER,
	"job_position_id"	INTEGER NOT NULL,
	"job_category_id"	INTEGER NOT NULL,
	"employment_type_id"	INTEGER,
	"location"	TEXT,
	"description"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("candidate_id") REFERENCES "candidate"("id"),
	FOREIGN KEY("company_id") REFERENCES "company"("id"),
	FOREIGN KEY("job_position_id") REFERENCES "job_position"("id"),
	FOREIGN KEY("job_category_id") REFERENCES "job_category"("id"),
	FOREIGN KEY("employment_type_id") REFERENCES "employment_type"("id")
);
CREATE TABLE IF NOT EXISTS "education" (
	"id"	INTEGER NOT NULL UNIQUE,
	"candidate_id"	INTEGER NOT NULL,
	"college_id"	INTEGER NOT NULL,
	"degree_id"	INTEGER NOT NULL,
	"date_start"	INTEGER,
	"date_end"	INTEGER,
	"description"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("candidate_id") REFERENCES "candidate"("id"),
	FOREIGN KEY("college_id") REFERENCES "college"("id"),
	FOREIGN KEY("degree_id") REFERENCES "degree"("id")
);
CREATE TABLE IF NOT EXISTS "application" (
	"id"	INTEGER NOT NULL UNIQUE,
	"date_of_application"	INTEGER NOT NULL,
	"job_opening_id"	INTEGER NOT NULL,
	"candidate_id"	INTEGER NOT NULL,
	"status"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("candidate_id") REFERENCES "candidate"("id"),
	FOREIGN KEY("job_opening_id") REFERENCES "job_opening"("id")
);
CREATE TABLE IF NOT EXISTS "candidate" (
	"id"	INTEGER NOT NULL UNIQUE,
	"first_name"	TEXT,
	"last_name"	TEXT,
	"email"	TEXT NOT NULL UNIQUE,
	"phone"	TEXT,
	"description"	TEXT,
	"pass_hash"	TEXT NOT NULL,
	"session_id"	INTEGER,
	"ethnicity_id"	INTEGER,
	"gender_id"	INTEGER,
	"gender_pronoun_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("ethnicity_id") REFERENCES "ethnicity"("id"),
	FOREIGN KEY("gender_id") REFERENCES "gender"("id"),
	FOREIGN KEY("gender_pronoun_id") REFERENCES "gender_pronoun"("id")
);
CREATE TABLE IF NOT EXISTS "interview" (
	"id"	INTEGER NOT NULL UNIQUE,
	"application_id"	INTEGER NOT NULL,
	"date_start"	INTEGER,
	"date_end"	INTEGER,
	"status"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("application_id") REFERENCES "application"("id")
);
CREATE TABLE IF NOT EXISTS "job_opening" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"description"	TEXT,
	"date_published"	INTEGER NOT NULL,
	"date_deadline"	INTEGER,
	"date_start_job"	INTEGER NOT NULL,
	"vacancy_count"	INTEGER,
	"job_category_id"	INTEGER NOT NULL,
	"job_position_id"	INTEGER NOT NULL,
	"company_id"	INTEGER NOT NULL,
  "process_id"	INTEGER,
	"recruiter_id"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("job_category_id") REFERENCES "job_category"("id"),
	FOREIGN KEY("job_position_id") REFERENCES "job_position"("id"),
	FOREIGN KEY("company_id") REFERENCES "company"("id"),
	FOREIGN KEY("process_id") REFERENCES "process"("id")
);
CREATE TABLE IF NOT EXISTS "process_step" (
	"id"	INTEGER NOT NULL UNIQUE,
	"process_id"	INTEGER NOT NULL,
	"title"	TEXT NOT NULL,
	"description"	TEXT,
	"required"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("process_id") REFERENCES "process"("id")
);
CREATE TABLE IF NOT EXISTS "college" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL,
	"description"	TEXT,
	"graduate"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "degree" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	"abbr"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	"years"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "industry" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "organization" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "major" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "skill" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "language" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ethnicity" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "gender_pronoun" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "gender" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "skill_candidate" (
	"id"	INTEGER NOT NULL UNIQUE,
	"candidate_id"	INTEGER NOT NULL,
	"skill_id"	INTEGER NOT NULL,
	FOREIGN KEY("candidate_id") REFERENCES "candidate"("id"),
	FOREIGN KEY("skill_id") REFERENCES "skill"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "language_candidate" (
	"id"	INTEGER NOT NULL UNIQUE,
	"candidate_id"	INTEGER NOT NULL,
	"language_id"	INTEGER NOT NULL,
	FOREIGN KEY("candidate_id") REFERENCES "candidate"("id"),
	FOREIGN KEY("language_id") REFERENCES "language"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
COMMIT;
