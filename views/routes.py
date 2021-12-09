from flask import Flask, request, jsonify
from flask_cors import CORS

#
# from models.schemas.candidate import Job Opening
from models.classes.candidate import Candidate
from models.classes.job_opening import JobOpening
from models.classes.application import Application

from .admin.singup_login_logout import login_user, signup_user, logout_user
# from .recruiter.recruiter_route import all_recruiters, get_a_recruiter
from .candidate.candidate_routes import list_candidates, get_candidate, update_candidate, delete_candidate
from .job_opening.job_opening_routes import list_job_openings, insert_job_opening, get_job_opening, update_job_opening, delete_job_opening
from .application.application_routes import list_applications, insert_application, get_application, update_application, delete_application
from .interview.interview_routes import list_interviews, insert_interview, get_interview, update_interview, delete_interview
from .experience.experience_routes import list_experiences, insert_experience, get_experience, update_experience, delete_experience
from .education.education_routes import list_educations, insert_education, get_education, update_education, delete_education

from models.classes.SQLTable import SQLTable
from .database.SQLTable_routes import get

app = Flask(__name__)
CORS(app)

# Pretty print JSON results
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# curl -X POST http://127.0.0.1:5000/api/signup -d '{"email":"test5@gmail.com","password":"21111"}'  -H "Content-Type: application/json"
@app.route("/api/signup", methods=["POST"])
def api_signup():
    return signup_user()

# curl -X POST http://127.0.0.1:5000/api/login -d '{"email":"test@gmail.com","password":"11111"}'  -H "Content-Type: application/json"
@app.route("/api/login", methods=["POST"])
def api_login():
    return login_user()

# curl -X POST http://127.0.0.1:5000/api/logout -d '{"session_id":"enter session_id here"}'  -H "Content-Type: application/json"
@app.route("/api/logout", methods=["POST"])
def api_logout():
    return logout_user()

# Get one row from a table
# curl -X GET http://127.0.0.1:5000/api/candidate/id/1
@app.route("/api/<table_name>/", methods=["GET"])
def api_get_list(table_name):
    argument_dict = request.args.to_dict()
    return get(table_name,argument_dict)

# Add a row to a table using id
@app.route("/api/<table_name>/add", methods=["POST"])
def api_insert():
    return insert()

# Delete a row from a table using id
@app.route("/api/<table_name>/delete/<id>", methods=["POST"])
def api_delete(table_name,id):
    return delete(table_name,id)
