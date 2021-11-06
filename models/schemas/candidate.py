# Candidate Schema
import sqlite3

class Candidate():

    tablename = "candidate"
    dbpath = "../data/test.db"

    def __init__(self, email, pass_hash, session_id, id = None, first_name = None, last_name = None, phone = None, description = None):
        self.id = id
        self.pass_hash = pass_hash
        self.session_id = session_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.description = description


    def insert_candidate(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO {self.tablename}
                      (first_name, last_name, email, phone, description, pass_hash, session_id)
                      VALUES (?,?,?,?,?,?,?);"""
            data = (self.first_name, self.last_name, self.email, self.phone, self.description, self.pass_hash, self.session_id)
            cursor.execute(sql, data)


    def update_candidate(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""UPDATE {self.tablename}
                      SET first_name = ?,
                          last_name = ?,
                          email = ?,
                          phone = ?,
                          description = ?,
                          pass_hash = ?,
                          session_id = ?
                      WHERE id = ?
                    """
            data = (self.first_name, self.last_name, self.email, self.phone, self.description, self.pass_hash, self.session_id, self.id)
            cursor.execute(sql, data)



    @classmethod
    def get_candidate(cls, email):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}
                    WHERE email = ?"""
            cursor.execute(sql, (email,))
        res =  cursor.fetchone()
        print(res)
        if res:
            user = Candidate(id = res[0], first_name=res[1], last_name=res[2],email=res[3],\
                             phone=res[4],description=res[5],pass_hash=res[6],session_id=res[7])
            return user
        return None


    # This function should be disabled in production.
    @classmethod
    def get_all_candidates(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}"""
            cursor.execute(sql)
        return cursor.fetchall()
