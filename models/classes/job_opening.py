# JobOpening Class Definition

import sqlite3

class JobOpening():
    tablename = "job_opening"
    dbpath = "../data/database.db"

    def __init__(self, id = None, name = None, description = None, date_published = None, date_deadline = None, date_start_job = None, vacancy_count = None, job_category_id = None, job_position_id = None, company_id = None, recruiter_id = None):
        self.id = id
        self.name = name
        self.description = description
        self.date_published = date_published
        self.date_deadline = date_deadline
        self.date_start_job = date_start_job
        self.vacancy_count = vacancy_count
        self.job_category_id = job_category_id
        self.job_position_id = job_position_id
        self.company_id = company_id
        self.recruiter_id = recruiter_id

    def insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO {self.tablename}
                      (name, description, date_published, date_deadline, date_start_job, vacancy_count, job_category_id, job_position_id, company_id, recruiter_id)
                      VALUES (?,?,?,?,?,?,?,?,?,?)"""
            data = (self.name, self.description, self.date_published, self.date_deadline, self.date_start_job, self.vacancy_count, self.job_category_id, self.job_position_id, self.company_id, self.recruiter_id)
            cursor.execute(sql, data)

    def update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""UPDATE {self.tablename}
                      SET name = ?,
                       description = ?,
                       date_published = ?,
                       date_deadline = ?,
                       date_start_job = ?,
                       vacancy_count = ?,
                       job_category_id = ?,
                       job_position_id = ?,
                       company_id = ?,
                       recruiter_id = ?,
                      WHERE id = ?
                    """
            data = (self.name, self.description, self.date_published, self.date_deadline, self.date_start_job, self.vacancy_count, self.job_category_id, self.job_position_id, self.company_id, self.recruiter_id, self.id)
            cursor.execute(sql, data)

    # Get a single job_opening given job_opening_id
    @classmethod
    def get(cls, id):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}
                    WHERE id = ?"""
            cursor.execute(sql, (id,))
        res =  cursor.fetchone()
        if res:
            job_opening = JobOpening(id = res[0],name = res[1], description = res[2], date_published = res[3], date_deadline = res[4], date_start_job = res[5], vacancy_count = res[6], job_category_id = res[7], job_position_id = res[8], company_id = res[9], recruiter_id = res[10])
            return job_opening
        return None

    # Get all job_openings for a recruiter given recruiter_id
    @classmethod
    def get_by_recruiter_id(cls, id):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}
                    WHERE recruiter_id = ?"""
            cursor.execute(sql, (recruiter_id))
        res =  cursor.fetchone()
        if res:
            job_opening = JobOpening(id = res[0],name = res[1], description = res[2], date_published = res[3], date_deadline = res[4], date_start_job = res[5], vacancy_count = res[6], job_category_id = res[7], job_position_id = res[8], company_id = res[9], recruiter_id = res[10])
            return job_opening
        return None

    # Get all job_openings in the database.
    # This function should be disabled in production.
    @classmethod
    def get_all(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}"""
            cursor.execute(sql)
        return cursor.fetchall()
