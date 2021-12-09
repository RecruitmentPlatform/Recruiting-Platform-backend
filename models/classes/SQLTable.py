# SQLTable Class Definition

import sqlite3
import abc

class SQLTable():
    dbpath = "../data/database.db"

    def __init__(self, id = None, name = None):
        self.id = id
        self.name = name

    def insert(self):
        value_list = []
        attributes = self.__dict__.items()
        for attribute, value in attributes:
            value_list.append(value)
        value_list.pop(0)
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            column_names = self.getColumnNames()
            column_string = ', '.join(column_names)
            value_string = ', '.join('?' * len(column_names))

            sql = '''INSERT INTO %s (%s) VALUES (%s)'''%(self.getTableName(),column_string, value_string)
            cursor.execute(sql, value_list)

    def delete(self, id, tableName = None):
        if not tableName:
            tableName = self.getTableName()
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = """DELETE FROM %s WHERE id = ?"""%(tableName)
            cursor.execute(sql, (id,))

    # Returns one single row from the database
    # SELECT JOIN WHERE
    # /api/<candidate>/ (post: {ethnicity_id: 1, company_id = 200})
    # company_id needs to be joined through experience which has company_id
    @classmethod
    def get(cls, tableName = None, argument_dict = None, limit = 25, offset = 0, sort = 'DESC'):
        print(argument_dict)
        #{id: 23523, name: weifjw}
        # loop over all of them
        # get the column names from the table im trying to insert to
        # find _id column names to get foreign keys
        # see if any of the data in the defined arguments tries to do a foreign key check
        # WHERE THIS = THAT AND
        # candidate {skill_id = 200, company_id = 50,  }
        if not tableName:
            tableName = cls.getTableName(cls)
        #valid_criteria = {"id","email","session_id"}
        #if criteria not in valid_criteria or not criteria_value:
            #return None
        # Define results
        results = []
        # Perform sql connection and execute command on the connection conn
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            #if criteria != "id":
                #criteria_value = "'" + criteria_value + "'"
            where = []
            sql = """SELECT * FROM %s WHERE %s = %s"""%(tableName,criteria,criteria_value)
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

    def getColumnNames(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = '''SELECT * FROM %s LIMIT 1'''%(self.getTableName())
            cursor.execute(sql)
            column_names = list(map(lambda x: x[0], cursor.description))
            column_names.remove("id")
            return column_names

    @abc.abstractmethod
    def getTableName(self):
        pass

# Candidate Data Classes
class Candidate(SQLTable):
    def __init__(self, email, pass_hash, session_id, id = None, first_name = None, last_name = None, phone = None, description = None, ethnicity_id = None, gender_id = None, gender_pronoun_id = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.description = description
        self.pass_hash = pass_hash
        self.session_id = session_id
        self.ethnicity_id = ethnicity_id
        self.gender_id = gender_id
        self.gender_pronoun_id = gender_pronoun_id

    def getTableName(self):
        return 'candidate'

class Ethnicity(SQLTable):
    def getTableName(self):
        return 'ethnicity'
class GenderPronoun(SQLTable):
    def getTableName(self):
        return 'gender_pronoun'
class Gender(SQLTable):
    def getTableName(self):
        return 'ethnicity'

# Education Data Classes
class Degree(SQLTable):
    def getTableName(self):
        return 'degree'
class Major(SQLTable):
    def getTableName(self):
        return 'major'
class College(SQLTable):
    def getTableName(self):
        return 'college'

# Job Opening Data Classes
class JobCategory(SQLTable):
    def getTableName(self):
        return 'job_category'
class JobPosition(SQLTable):
    def getTableName(self):
        return 'job_position'
class Company(SQLTable):
    def getTableName(self):
        return 'company'
