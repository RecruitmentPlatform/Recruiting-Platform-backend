# Candidate Class Definition

import sqlite3

class Account():
    tablename = "candidate"
    dbpath = "../data/database.db"

    def __init__(self, email, pass_hash, session_id, id = None, first_name = None, last_name = None, phone = None, description = None, ethnicity_id = None, gender_id = None, gender_pronoun_id = None):
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

class Candidate(Account):
    def insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO {self.tablename}
                      (first_name, last_name, email, phone, description, pass_hash, session_id, ethnicity_id, gender_id, gender_pronoun_id)
                      VALUES (?,?,?,?,?,?,?,?,?,?)"""
            data = (self.first_name, self.last_name, self.email, self.phone, self.description, self.pass_hash, self.session_id, self.ethnicity_id, self.gender_id, self.gender_pronoun_id)
            cursor.execute(sql, data)

    def update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""UPDATE {self.tablename}
                      SET first_name = ?, last_name = ?, email = ?, phone = ?, description = ?, pass_hash = ?, session_id = ?, ethnicity_id = ?, gender_id = ?, gender_pronoun_id = ?
                      WHERE id = ?"""
            data = (self.first_name, self.last_name, self.email, self.phone, self.description, self.pass_hash, self.session_id, self.ethnicity_id, self.gender_id, self.gender_pronoun_id, self.id)
            cursor.execute(sql, data)

    def delete(self, id):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""DELETE
                      FROM {self.tablename}
                      WHERE id = ?"""
            cursor.execute(sql, (id,))

    @classmethod
    def get(cls, criteria, data):
        #print(criteria, data)
        if criteria == "email":
            return Candidate.query("email", data)
        elif criteria == "session_id":
            return Candidate.query("session_id", data)
        elif criteria == "id":
            return Candidate.query("id", data)

    @classmethod
    def query(cls, criteria, data):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}
                    WHERE {criteria} = ?"""
            cursor.execute(sql, data)
        res =  cursor.fetchone()
        if res:
            user = Candidate(id = res[0],first_name=res[1], last_name=res[2],email=res[3],phone=res[4],description=res[5],pass_hash=res[6],session_id=res[7],ethnicity_id=res[8],gender_id=res[9],gender_pronoun_id=res[10])
            return user
        return None

    #################################################
    # For debug -->
    # This function should be disabled in production.
    @classmethod
    def get_all(cls):
        # Define results
        results = []
        # Perform sql connection and execute command on the connection conn
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            sql = f"""SELECT * FROM {cls.tablename}"""
            cursor.execute(sql)
        # Save sql results
        rows =  cursor.fetchall()
        # Define columns that should not be returned publicly
        private_columns = {'pass_hash','session_id'}
        # Iterate over sql results
        for row in rows:
            # Create list to save row values within
            result = {}
            # Get sql results column names
            columns = row.keys()
            # Loop over the sql result column names
            for column in columns:
                # Skip private columns
                if column in private_columns:
                    continue
                # Use column names to index sql results and save in result list
                result[column] = row[column]
            # Append entire result to results array
            results.append(result)
        return results
