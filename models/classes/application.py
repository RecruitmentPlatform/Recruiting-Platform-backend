# Application Class Definition

import sqlite3

class Application():
    tablename = "application"
    dbpath = "../data/database.db"

    def __init__(self, date_of_application, job_opening_id, candidate_id, id = None, status = 0):
        self.id = id
        self.date_of_application = date_of_application
        self.job_opening_id = job_opening_id
        self.candidate_id = candidate_id
        self.status = status

    def insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO {self.tablename}
                      (date_of_application, job_opening_id, candidate_id, status)
                      VALUES (?,?,?,?)"""
            data = (self.date_of_application, self.job_opening_id, self.candidate_id, self.status)
            cursor.execute(sql, data)


    def update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""UPDATE {self.tablename}
                      SET date_of_application = ?,
                          job_opening_id = ?,
                          candidate_id = ?,
                          status = ?
                      WHERE id = ?
                    """
            data = (self.date_of_application, self.job_opening_id, self.candidate_id, self.status, self.id)
            cursor.execute(sql, data)

    # Get a single application given application_id
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
            application = Application(id = res[0], date_of_application = res[1], job_opening_id = res[2], candidate_id = res[3], status = res[4])
            return application
        return None

    # Get all applications for a job_opening given job_opening_id
    @classmethod
    def get_by_recruiter_id(cls, job_opening_id):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}
                    WHERE job_opening_id = ?"""
            cursor.execute(sql, (job_opening_id,))
        res =  cursor.fetchone()
        if res:
            application = Application(id = res[0], date_of_application = res[1], job_opening_id = res[2], candidate_id = res[3], status = res[4])
            return application
        return None

    # Get all applications for a candidate given candidate_id
    @classmethod
    def get_by_candidate_id(cls, candidate_id):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}
                    WHERE candidate_id = ?"""
            cursor.execute(sql, (candidate_id))
        res =  cursor.fetchone()
        if res:
            application = Application(id = res[0], date_of_application = res[1], job_opening_id = res[2], candidate_id = res[3], status = res[4])
            return application
        return None

    # Get all applications in the database.
    # This function should be disabled in production.
    @classmethod
    def get_all(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}"""
            cursor.execute(sql)
        return cursor.fetchall()
