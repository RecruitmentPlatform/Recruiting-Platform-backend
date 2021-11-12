# Recruiter Class Definition

import sqlite3

class Recruiter():
    tablename = "recruiter"
    dbpath = "../data/database.db"

    def __init__(self, id = None, first_name = None, last_name = None, email,  phone = None, description = None, pass_hash, session_id, ethnicity_id = None, gender_id = None, gender_pronoun_id = None):
        self.id = id
        self.pass_hash = pass_hash
        self.session_id = session_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.description = description
        self.ethnicity_id = ethnicity_id
        self.gender_id = gender_id
        self.gender_pronoun_id = gender_pronoun_id

    def insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO {self.tablename}
                      (first_name, last_name, email, phone, description, pass_hash, session_id, ethnicity_id, gender_id, gender_pronoun_id)
                      VALUES (?,?,?,?,?,?,?,?,?,?,?)"""
            data = (self.first_name, self.last_name, self.email, self.phone, self.description, self.pass_hash, self.session_id, self.ethnicity_id, self.gender_id, self.gender_pronoun_id)
            cursor.execute(sql, data)

    def update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""UPDATE {self.tablename}
                      SET first_name = ?,
                          last_name = ?,
                          email = ?,
                          phone = ?,
                          description = ?,
                          pass_hash = ?,
                          session_id = ?,
                          ethnicity_id = ?,
                          gender_id = ?,
                          gender_pronoun_id = ?
                      WHERE id = ?
                    """
            data = (self.first_name, self.last_name, self.email, self.phone, self.description, self.pass_hash, self.session_id, self.ethnicity_id, self.gender_id, self.gender_pronoun_id, self.id)
            cursor.execute(sql, data)

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
            user = Recruiter(id = res[0])
            return user
        return None

    # This function should be disabled in production.
    @classmethod
    def get_all(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}"""
            cursor.execute(sql)
        return cursor.fetchall()
