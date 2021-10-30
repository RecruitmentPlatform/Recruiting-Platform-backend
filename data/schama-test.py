import sqlite3
import os

PATH = os.path.dirname(__file__)
DATAPATH = os.path.join(PATH, "test.db")

def schema(dbpath = DATAPATH):
    with sqlite3.connect(DATAPATH) as conn: # object to represent DB connection
        cursor = conn.cursor()
        sql = """CREATE TABLE IF NOT EXISTS candidate (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                first_name TEXT,
                last_name	TEXT,
                email	TEXT NOT NULL,
                phone	TEXT,
                description	TEXT,
                pass_hash	TEXT NOT NULL,
                session_id	TEXT NOT NULL
            );"""
        cursor.execute(sql)

if __name__ == "__main__":
    schema() 

