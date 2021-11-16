# Education Class Definition

import sqlite3

class Education():
    tablename = "education"
    dbpath = "../data/database.db"

    def __init__(self, candidate_id, college_id = None, degree_id = None, date_start = None, date_end = None, major_id = None):
        self.id = id
        self.candidate_id = candidate_id
        self.college_id = college_id
        self.degree_id = degree_id
        self.date_start = date_start
        self.date_end = date_end
        self.major_id = major_id

    def insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO {self.tablename}
                      (candidate_id, college_id, degree_id, date_start, date_end, major_id)
                      VALUES (?,?,?,?,?,?,?);"""
            data = (self.candidate_id, self.college_id, self.degree_id, self.date_start, self.date_end, self.major_id)
            cursor.execute(sql, data)

    def update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""UPDATE {self.tablename}
                      SET candidate_id = ?,
                        college_id = ?,
                        degree_id = ?,
                        date_start = ?,
                        date_end = ?,
                        major_id = ?
                        WHERE id = ?;"""
            data = (self.candidate_id, self.college_id, self.degree_id, self.date_start, self.date_end, self.major_id, self.id)
            cursor.execute(sql, data)

    # Get a single education given education_id
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
            education = Education(id = res[0],candidate_id = res[1], college_id = res[2], degree_id = res[3], date_start = res[4], date_end = res[5], major_id = res[6])
            return education
        return None

    # Get all educations for a candidate given candidate_id
    @classmethod
    def get_by_candidate_id(cls, id):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}
                    WHERE candidate_id = ?"""
            cursor.execute(sql, (candidate_id,))
        res =  cursor.fetchone()
        if res:
            education = Education(id = res[0],candidate_id = res[1], college_id = res[2], degree_id = res[3], date_start = res[4], date_end = res[5], major_id = res[6])
            return education
        return None

    # Get all educations in the database.
    # This function should be disabled in production.
    @classmethod
    def get_all(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}"""
            cursor.execute(sql)
        return cursor.fetchall()
