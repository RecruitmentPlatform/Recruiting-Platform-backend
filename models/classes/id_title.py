# ID Title Class Definition

import sqlite3
import abc

class Data():
    dbpath = "../data/database.db"

    def __init__(self, id = None, name = None):
        self.id = id
        self.name = name

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

    @abc.abstractmethod
    def get_tablename(self):
        pass

# Candidate Data Classes
class Ethnicity(Data):
    def get_tablename(self):
        return 'ethnicity'
class GenderPronoun(Data):
    def get_tablename(self):
        return 'gender_pronoun'
class Gender(Data):
    def get_tablename(self):
        return 'ethnicity'

# Education Data Classes
class Degree(Data):
    def get_tablename(self):
        return 'degree'
class Major(Data):
    def get_tablename(self):
        return 'major'
class College(Data):
    def get_tablename(self):
        return 'college'

# Job Opening Data Classes
class JobCategory(Data):
    def get_tablename(self):
        return 'job_category'
class JobPosition(Data):
    def get_tablename(self):
        return 'job_position'
class Company(Data):
    def get_tablename(self):
        return 'company'
