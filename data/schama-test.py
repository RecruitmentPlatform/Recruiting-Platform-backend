import sqlite3
import os

PATH = os.path.dirname(__file__)
DATAPATH = os.path.join(PATH, "database.db")

def schema(dbpath = DATAPATH):
    with sqlite3.connect(DATAPATH) as conn: # object to represent DB connection
        cursor = conn.cursor()
        sql = """CREATE TABLE IF NOT EXISTS candidate (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name	TEXT,
                email	TEXT NOT NULL,
                phone	TEXT,
                description	TEXT,
                pass_hash	TEXT NOT NULL,
                session_id	TEXT
            );"""
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS recruiter (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name	TEXT,
                email	TEXT NOT NULL,
                pass_hash	TEXT NOT NULL,
                session_id	TEXT
            );"""
        cursor.execute(sql)



if __name__ == "__main__":
    schema()
