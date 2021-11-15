import os
from views.routes import app

from models.classes.candidate import Candidate
from models.classes.job_opening import JobOpening
from models.classes.application import Application
from models.classes.interview import Interview

PATH = os.path.dirname(__file__)
Candidate.dbpath = os.path.join(PATH, "data", "database.db")
JobOpening.dbpath = os.path.join(PATH, "data", "database.db")
Application.dbpath = os.path.join(PATH, "data", "database.db")
Interview.dbpath = os.path.join(PATH, "data", "database.db")

if __name__ == "__main__":
    app.run()
