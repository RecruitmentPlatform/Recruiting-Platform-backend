BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "companies" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	"location" TEXT,
	"website" TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "employments" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "experiences" (
	"id"	INTEGER NOT NULL UNIQUE,
	"candidate_id"	INTEGER NOT NULL,
	"title"	TEXT NOT NULL,
	"company_name"	TEXT,
	"company_id"	INTEGER,
	"start_month"	INTEGER,
	"start_year"	INTEGER,
	"end_month"	INTEGER,
	"end_year"	INTEGER,
	"employment_id"	INTEGER,
	"location"	TEXT,
	"description"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "educations" (
	"id"	INTEGER NOT NULL UNIQUE,
	"candidate_id"	INTEGER NOT NULL,
	"college_name" TEXT NOT NULL,
	"college_id"	INTEGER,
	"degree" TEXT,
	"degree_id"	INTEGER,
	"start_month"	INTEGER,
	"start_year"	INTEGER,
	"end_month"	INTEGER,
	"end_year"	INTEGER,
	"description"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "applications" (
	"id"	INTEGER NOT NULL UNIQUE,
	"date"	INTEGER NOT NULL,
	"opening_id"	INTEGER NOT NULL,
	"candidate_id"	INTEGER NOT NULL,
	"status"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "candidates" (
	"id"	INTEGER NOT NULL UNIQUE,
	"first"	TEXT,
	"last"	TEXT,
	"email"	TEXT NOT NULL UNIQUE,
	"phone"	TEXT,
	"description"	TEXT,
	"location" TEXT,
	"headline" TEXT,
	"hash"	TEXT NOT NULL,
	"session"	INTEGER,
	"ethnicity_id"	INTEGER,
	"gender_id"	INTEGER,
	"pronoun_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "interviews" (
	"id"	INTEGER NOT NULL UNIQUE,
	"application_id"	INTEGER NOT NULL,
	"start"	INTEGER,
	"end"	INTEGER,
	"status"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "colleges" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL,
	"description"	TEXT,
	"graduate"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "degrees" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	"abbr"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	"years"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "industries" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "organizations" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "majors" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ethnicities" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "pronouns" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "genders" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "openings" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL,
	"date" INTEGER NOT NULL,
	"company_name" TEXT NOT NULL,
	"description"	TEXT,
	"location" TEXT,
	"published"	INTEGER NOT NULL,
	"deadline"	INTEGER,
	"salary_low" INTEGER,
	"salary_high" INTEGER,
	"start_month"	INTEGER,
	"start_year"	INTEGER,
	"vacancy"	INTEGER,
	"company_id"	INTEGER,
	"candidate_id"	INTEGER NOT NULL,
	"employment_id" INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "posts" (
	"id" INTEGER NOT NULL,
	"candidate_id" INTEGER NOT NULL,
	"date" INTEGER NOT NULL,
	"status" INTEGER NOT NULL,
	"content" TEXT NOT NULL,
	"opening_id" INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "skills" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	"skilltype_id" INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "skilltypes" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "skill_candidate" (
	"id" INTEGER NOT NULL UNIQUE,
	"skill_id" INTEGER NOT NULL,
	"candidate_id" INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "candidate_company" (
	"id" INTEGER NOT NULL UNIQUE,
	"candidate_id" INTEGER NOT NULL,
	"company_id" INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
COMMIT;
