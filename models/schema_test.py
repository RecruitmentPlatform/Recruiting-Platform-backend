import sqlite3

class Candidate():

    tablename = "candidate"
    dbpath = "../data/test.db"

    def __init__(self, username, email, pass_hash, session_id, id = None, first_name = None, last_name = None, phone = None, description = None):
        self.id = id
        self.username = username
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
                      (username, first_name, last_name, email, phone, description, pass_hash, session_id)
                      VALUES (?,?,?,?,?,?,?,?);"""
            data = (self.username, self.first_name, self.last_name, self.email, self.phone, self.description, self.pass_hash, self.session_id)
            cursor.execute(sql, data)


    @classmethod
    def get_candidate(cls, username):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}
                    WHERE username = ?"""
            cursor.execute(sql, (username,))
        return cursor.fetchone()


    @classmethod
    def get_all_candidates(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT * 
                    FROM {cls.tablename}"""
            cursor.execute(sql)
        return cursor.fetchall()

    
