# Experience Class Definition

import sqlite3

class Experience():
    tablename = "experience"
    dbpath = "../data/database.db"

    def __init__(self, id = None, name = None, description = None, date_published = None, date_deadline = None, date_start_job = None, vacancy_count = None, job_category_id = None, job_position_id = None, company_id = None, recruiter_id = None):
        self.id = id
        self.candidate_id
        self.company_id
        self.date_start
        self.date_end
        self.job_position_id
        self.job_category_id
        self.employment_type_id
        self.location
        self.description

    def insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO {self.tablename}
                      (id, candidate_id, company_id, date_start, date_end, job_position_id, job_category_id, employment_type_id, location, description)
                      VALUES (?,?,?,?,?,?,?,?,?,?);"""
            data = (self.candidate_id, self.company_id, self.date_start, self.date_end, self.job_position_id, self.job_category_id, self.employment_type_id, self.location, self.description)
            cursor.execute(sql, data)

    def update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""UPDATE {self.tablename}
                      SET candidate_id = ?,
                        company_id = ?,
                        date_start = ?,
                        date_end = ?,
                        job_position_id = ?,
                        job_category_id = ?,
                        employment_type_id = ?,
                        location = ?,
                        description = ?
                        WHERE id = ?;"""
            data = (self.candidate_id, self.company_id, self.date_start, self.date_end, self.job_position_id, self.job_category_id, self.employment_type_id, self.location, self.description, self.id)
            cursor.execute(sql, data)

    # Get a single experience given experience_id
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
            experience = Experience(id = res[0], candidate_id = res[1], company_id = res[2], date_start = res[3], date_end = res[4], job_position_id = res[5], job_category_id = res[6], employment_type_id = res[7], location = res[8], description = res[9])
            return experience
        return None

    # Get all experiences for a recruiter given candidate_id
    @classmethod
    def get_by_recruiter_id(cls, id):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}
                    WHERE candidate_id = ?"""
            cursor.execute(sql, (candidate_id))
        res =  cursor.fetchone()
        if res:
            experience = Experience(id = res[0], candidate_id = res[1], company_id = res[2], date_start = res[3], date_end = res[4], job_position_id = res[5], job_category_id = res[6], employment_type_id = res[7], location = res[8], description = res[9])
            return experience
        return None

    # Get all experiences in the database.
    # This function should be disabled in production.
    @classmethod
    def get_all(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}"""
            cursor.execute(sql)
        return cursor.fetchall()
