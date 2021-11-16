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

app = Flask(__name__)
CORS(app)

# Pretty print JSON results
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# curl -X POST http://127.0.0.1:5000/api/signup -d '{"email":"test2@gmail.com","password":"21111"}'  -H "Content-Type: application/json"
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
@app.route("/api/candidates/", methods=["GET"])
def api_list_candidates():
    return list_candidates()

# Get a single candidate that matches the id
#curl -X GET http://127.0.0.1:5000/api/candidates/1
@app.route("/api/candidates/<criteria>/<criteria_id>", methods=["GET"])
def api_get_candidate(criteria_id,criteria="id"):
    return get_candidate(criteria_id, criteria)

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

#################################
## Interview Endpoints ##

# Get a list of all interviews
# curl -X GET http://127.0.0.1:5000/api/interviews
@app.route("/api/interviews/", methods=["GET"])
def api_list_interviews():
    return list_interviews()

# Get a single interview that matches the id
# curl -X GET http://127.0.0.1:5000/api/interviews/1
@app.route("/api/interviews/<interview_id>", methods=["GET"])
def api_get_interview(interview_id):
    return get_interview(interview_id)

# Add an interview record
# curl -X POST http://127.0.0.1:5000/api/interviews/add -d '{"application_id": 12345, "date_start": 12345, "date_end": 56789, "status": 1}' -H "Content-Type: application/json"
@app.route("/api/interviews/add", methods=["POST"])
def api_insert_interview():
    return insert_interview()

# Update an interview record
@app.route("/api/interviews/update", methods=["PUT"])
def api_update_interview():
    return update_interview()

# Delete an interview record that matches the id
@app.route("/api/interviews/delete/<interview_id>", methods=["GET"])
def api_delete_interview(interview_id):
    return delete_interview(interview_id)


#################################
## Experience Endpoints ##

# Get a list of all experiences
# curl -X GET http://127.0.0.1:5000/api/experiences
@app.route("/api/experiences/", methods=["GET"])
def api_list_experience():
    return list_experience()

# Get a single experience that matches the id
# curl -X GET http://127.0.0.1:5000/api/experiences/1
@app.route("/api/experiences/<experience_id>", methods=["GET"])
def api_get_experience(experience_id):
    return get_experience(experience_id)

# Add an experience record
# curl -X POST http://127.0.0.1:5000/api/experiences/add -d '{}' -H "Content-Type: application/json"
@app.route("/api/experiences/add", methods=["POST"])
def api_insert_experience():
    return insert_experience()

# Update an experience record
@app.route("/api/experiences/update", methods=["PUT"])
def api_update_experience():
    return update_experience()

# Delete an experience record that matches the id
@app.route("/api/experiences/delete/<experience_id>", methods=["GET"])
def api_delete_experience(experience_id):
    return delete_experience(experience_id)

#################################
## Education Endpoints ##

# Get a list of all educations
# curl -X GET http://127.0.0.1:5000/api/educations
@app.route("/api/educations/", methods=["GET"])
def api_list_education():
    return list_education()

# Get a single education that matches the id
# curl -X GET http://127.0.0.1:5000/api/educations/1
@app.route("/api/educations/<education_id>", methods=["GET"])
def api_get_education(education_id):
    return get_education(education_id)

# Add an education record
# curl -X POST http://127.0.0.1:5000/api/education/add -d '{}' -H "Content-Type: application/json"
@app.route("/api/educations/add", methods=["POST"])
def api_insert_education():
    return insert_education()

# Update an education record
@app.route("/api/educations/update", methods=["PUT"])
def api_update_education():
    return update_education()

# Delete an education record that matches the id
@app.route("/api/educations/delete/<education_id>", methods=["GET"])
def api_delete_education(education_id):
    return delete_education(education_id)
