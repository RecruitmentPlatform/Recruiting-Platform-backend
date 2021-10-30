import os
from views.routes import app

from models.schema_test import Candidate

PATH = os.path.dirname(__file__)
Candidate.dbpath = os.path.join(PATH, "data", "test.db")

if __name__ == "__main__":
    app.run()