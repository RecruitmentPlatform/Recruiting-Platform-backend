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

app = Flask(__name__)
CORS(app)

# Pretty print JSON results
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

#curl -X POST http://127.0.0.1:5000/api/signup -d '{"email":"test@gmail.com","password":"11111"}'  -H "Content-Type: application/json"
@app.route("/api/signup", methods=["POST"])
def api_signup():
    return signup_user()

#curl -X POST http://127.0.0.1:5000/api/login -d '{"email":"test@gmail.com","password":"11111"}'  -H "Content-Type: application/json"
@app.route("/api/login", methods=["POST"])
def api_login():
    return login_user()

#curl -X POST http://127.0.0.1:5000/api/logout -d '{"session_id":"enter session_id here"}'  -H "Content-Type: application/json"
@app.route("/api/logout", methods=["POST"])
def api_logout():
    return logout_user()

## Company Endpoints ##

# Get a list of all companies
# @app.route("/api/companies", methods=["GET"])

# Get a single company that matches the id
# @app.route("/api/companies/<company_id>", methods=["GET"])

# Add a company record
# @app.route("/api/companies/add", methods=["GET"])

# Update a company record
# @app.route("/api/companies/update", methods=["GET"])

## Recruiter Endpoints ##

# Get a list of all recruiters
# @app.route("/api/recruiters", methods=["GET"])
# def get_all_recruiters():
#     return all_recruiters()


# Get a single recruiter that matches the id
# @app.route("/api/recruiters/<recruiter_id>", methods=["GET"])
# def get_recruiter():
#     return get_a_recruiter()


# Add a recruiter record
# @app.route("/api/recruiters/add", methods=["GET"])

# Update a recruiter record
# @app.route("/api/recruiters/update", methods=["GET"])

# Delete a recruiter record that matches the id
# @app.route("/api/recruiters/delete/<recruiter_id>", methods=["GET"])

#################################
## Candidate Endpoints ##

# Get a list of all candidates
# curl -X GET http://127.0.0.1:5000/api/candidates
@app.route("/api/candidates/all", methods=["GET"])
def api_list_candidates():
    return list_candidates()

# Get a single candidate that matches the id
#curl -X GET http://127.0.0.1:5000/api/candidates/1
@app.route("/api/candidates/<candidate_id>/<criteria>", methods=["GET"])
def api_get_candidate(candidate_id,criteria="id"):
    return get_candidate(candidate_id, criteria)

# Update a candidate record
# curl -X PUT http://127.0.0.1:5000/api/candidates/update -d '{"first_name":"test", "last_name":"user", "email":"", "phone":"1234567", "description":"swe", "session_id"}' -H "Content-Type: application/json"
@app.route("/api/candidates/update", methods=["PUT"])
def api_update_candidate():
    return update_candidate()

# Delete a candidate record that matches the id
#curl -X "DELETE" http://127.0.0.1:5000/api/candidates/delete/1
@app.route("/api/candidates/delete/<candidate_id>", methods=["DELETE"])
def api_delete_candidate(candidate_id):
    return delete_candidate(candidate_id)

#################################
## Job Opening Endpoints ##

# Get a list of all job openings
# curl -X GET http://127.0.0.1:5000/api/job-openings
@app.route("/api/job-openings/", methods=["GET"])
def api_list_job_openings():
    return list_job_openings()

# Get a single job opening that matches the id
# curl -X GET http://127.0.0.1:5000/api/candidates/1
@app.route("/api/job-openings/<job_opening_id>", methods=["GET"])
def api_get_job_opening(job_opening_id):
    return get_job_opening(job_opening_id)

# Add a job opening record
# curl -X POST http://127.0.0.1:5000/api/job-openings/add -d '{"name":"software engineer", "description": "job description", "date_published": 12345, "date_deadline": 56789, "date_start_job": 34567, "vacancy_count": 2, "job_category_id": 2, "job_position_id": 2, "company_id": 2, "recruiter_id": 2}' -H "Content-Type: application/json"
@app.route("/api/job-openings/add", methods=["POST"])
def api_insert_job_opening():
    return insert_job_opening()

# Update a job opening record
@app.route("/api/job-openings/update", methods=["PUT"])
def api_update_job_opening():
    return update_job_opening()

# Delete a job opening record that matches the id
@app.route("/api/job-openings/delete/<job_opening_id>", methods=["GET"])
def api_delete_job_opening(job_opening_id):
    return delete_job_opening(job_opening_id)


#################################
## Application Endpoints ##

# Get a list of all applications
# curl -X GET http://127.0.0.1:5000/api/applications
@app.route("/api/applications/", methods=["GET"])
def api_list_applications():
    return list_applications()

# Get a single application that matches the id
# curl -X GET http://127.0.0.1:5000/api/applications/1
@app.route("/api/applications/<application_id>", methods=["GET"])
def api_get_application(application_id):
    return get_application(application_id)

# Add an application record
# curl -X POST http://127.0.0.1:5000/api/applications/add -d '{"date_of_application": 12345, "job_opening_id": 12345, "candidate_id": 56789, "status": 1}' -H "Content-Type: application/json"
@app.route("/api/applications/add", methods=["POST"])
def api_insert_application():
    return insert_application()

# Update an application record
@app.route("/api/applications/update", methods=["PUT"])
def api_update_application():
    return update_application()

# Delete an application record that matches the id
@app.route("/api/applications/delete/<application_id>", methods=["GET"])
def api_delete_application(application_id):
    return delete_application(application_id)

# Get all applications for a job given the job opening ID
# @app.route("/api/applications/<job_opening_id>", methods=["GET"])

# Get all applications for a candidate given the candidate ID
# @app.route("/api/applications/<job_opening_id>", methods=["GET"])
