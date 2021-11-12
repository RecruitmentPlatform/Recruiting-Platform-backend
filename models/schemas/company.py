# Company Class Definition

import sqlite3

class Company():
    tablename = "company"
    dbpath = "../data/database.db"

    def __init__(self, id = None, name = None, description = None):
        self.id = id
        self.name = name
        self.description = description

    def insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO {self.tablename}
                      (name, description)
                      VALUES (?,?)"""
            data = (self.name = name, self.description = description)
            cursor.execute(sql, data)

    def update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""UPDATE {self.tablename}
                      SET name = ?,
                          description = ?
                      WHERE id = ?
                    """
            data = (self.name = name, self.description = description, self.id)
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
            user = Company(id = res[0])
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
