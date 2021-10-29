BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "company" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "employment_types" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "job_category" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "job_position" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "process" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "recruiter" (
	"id"	INTEGER NOT NULL UNIQUE,
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	"pass_hash"	TEXT NOT NULL,
	"session_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "experience" (
	"id"	INTEGER NOT NULL UNIQUE,
	"candidate_id"	INTEGER NOT NULL,
	"company_id"	INTEGER NOT NULL,
	"date_start"	INTEGER NOT NULL,
	"date_end"	INTEGER NOT NULL,
	"job_position_id"	INTEGER NOT NULL,
	"job_category_id"	INTEGER NOT NULL,
	"location"	TEXT NOT NULL,
	"employment_type_id"	INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("candidate_id") REFERENCES "candidate"("id"),
	FOREIGN KEY("job_position_id") REFERENCES "job_position"("id"),
	FOREIGN KEY("job_category_id") REFERENCES "job_category"("id"),
	FOREIGN KEY("employment_type_id") REFERENCES "employment_types"("id")
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
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	"phone"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	"pass_hash"	TEXT NOT NULL,
	"session_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "interview" (
	"id"	INTEGER NOT NULL UNIQUE,
	"start_time"	INTEGER NOT NULL,
	"end_time"	INTEGER NOT NULL,
	"application_id"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("application_id") REFERENCES "application"("id")
);
CREATE TABLE IF NOT EXISTS "job_opening" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	"date_published"	INTEGER NOT NULL,
	"job_start_date"	INTEGER NOT NULL,
	"no_of_vacancies"	INTEGER NOT NULL,
	"job_category_id"	INTEGER NOT NULL,
	"job_position_id"	INTEGER NOT NULL,
	"company_id"	INTEGER NOT NULL,
	"process_id"	INTEGER NOT NULL,
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
	"description"	TEXT NOT NULL,
	"required"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("process_id") REFERENCES "process"("id")
);
COMMIT;
