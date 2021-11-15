# Interview Class Definition

import sqlite3

class Interview():
    tablename = "interview"
    dbpath = "../data/database.db"

    def __init__(self, application_id, id = None, date_start = None, date_end = None, status = 0):
        self.id = id
        self.application_id = application_id
        self.date_start = date_start
        self.date_end = date_end
        self.status = status

    def insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO {self.tablename}
                      (application_id, date_start, date_end, status)
                      VALUES (?,?,?,?)"""
            data = (self.application_id, self.date_start, self.date_end, self.status)
            cursor.execute(sql, data)

    def update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""UPDATE {self.tablename}
                      SET application_id = ?,
                          date_start = ?,
                          date_end = ?,
                          status = ?
                      WHERE id = ?
                    """
            data = (self.application_id, self.date_start, self.date_end, self.status, self.id)
            cursor.execute(sql, data)

    # Get a single interview given interview_id
    @classmethod
    def get(cls, id):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}
                    WHERE id = ?"""
            cursor.execute(sql, (id))
        res =  cursor.fetchone()
        if res:
            interview = Interview(id = res[0], application_id = res[1], date_start = res[2], date_end = res[3], status = res[4])
            return interview
        return None

    # Get all interviews for a recruiter given recruiter_id
    @classmethod
    def get_by_recruiter_id(cls, id):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}
                    INNER JOIN application
                        ON application.id = {cls.tablename}.application_id
                    INNER JOIN job_opening
                        ON job_opening.id = application.job_opening_id
                    WHERE job_opening.recruiter_id = ?"""
            cursor.execute(sql, (recruiter_id))
        res =  cursor.fetchone()
        if res:
            interview = Interview(id = res[0], application_id = res[1], date_start = res[2], date_end = res[3], status = res[4])
            return interview
        return None

    # Get all interviews for a candidate given candidate_id
    @classmethod
    def get_by_candidate_id(cls, id):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}
                    INNER JOIN applications
                        ON applications.id = {cls.tablename}.application_id
                    WHERE applications.candidate_id = ?"""
            cursor.execute(sql, (candidate_id))
        res =  cursor.fetchone()
        if res:
            interview = Interview(id = res[0], application_id = res[1], date_start = res[2], date_end = res[3], status = res[4])
            return interview
        return None

    # Get all interviews in the database.
    # This function should be disabled in production.
    @classmethod
    def get_all(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}"""
            cursor.execute(sql)
        return cursor.fetchall()
