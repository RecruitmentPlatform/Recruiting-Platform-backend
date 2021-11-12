import os
from views.routes import app

from models.schemas.candidate import Candidate

PATH = os.path.dirname(__file__)
Candidate.dbpath = os.path.join(PATH, "data", "database.db")

if __name__ == "__main__":
    app.run()
