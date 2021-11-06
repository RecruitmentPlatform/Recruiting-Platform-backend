#Recruiter Schema
import sqlite3

class Recruiter():

    tablename = "recruiter"
    dbpath = "../data/test.db"

    def __init__(self, email, pass_hash, session_id, id = None, first_name = None, last_name = None):
        self.id = id
        self.pass_hash = pass_hash
        self.session_id = session_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


    def insert_recruiter(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO {self.tablename}
                      (first_name, last_name, email, pass_hash, session_id)
                      VALUES (?,?,?,?,?);"""
            data = (self.first_name, self.last_name, self.email, self.pass_hash, self.session_id)
            cursor.execute(sql, data)


    def update_recruiter(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""UPDATE {self.tablename}
                      SET first_name = ?,
                          last_name = ?,
                          email = ?,
                          pass_hash = ?,
                          session_id = ?
                      WHERE id = ?
                    """
            data = (self.first_name, self.last_name, self.email, self.pass_hash, self.session_id, self.id)
            cursor.execute(sql, data)


    @classmethod
    def get_recruiter_by_email(cls, email):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}
                    WHERE email = ?"""
            cursor.execute(sql, (email,))
        res =  cursor.fetchone()
        if res:
            user = Recruiter(id = res[0], first_name=res[1], last_name=res[2],\
                             email=res[3], pass_hash=res[4], session_id=res[5])
            return user
        return None


    @classmethod
    def get_recruiter_by_session_id(cls, session_id):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}
                    WHERE session_id = ?"""
            cursor.execute(sql, (session_id,))
        res =  cursor.fetchone()
        if res:
            user = Recruiter(id = res[0], first_name=res[1], last_name=res[2],\
                             email=res[3],pass_hash=res[6],session_id=res[7])
            return user
        return None


    @classmethod
    def get_all_recruiters(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}"""
            cursor.execute(sql)
        return cursor.fetchall()
