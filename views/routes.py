from flask import Flask, request, jsonify
from flask_cors import CORS

# from models.settings import session
from models.utils import hash_password, verify_password, generate_session_id

#
# from models.schemas.candidate import Job Opening
from models.schemas.candidate import Candidate

app = Flask(__name__)
CORS(app)

#curl -X POST http://127.0.0.1:5000/api/signup -d '{"username":"test","email":"test@gmail.com","password":"11111"}'  -H "Content-Type: application/json"
@app.route("/api/signup", methods=["POST"])
def signup():

    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Query database to see if user already exists
    user = Candidate.get_candidate(username)
    if user:
        return jsonify({"status":"fail", "message":"Account already exists"})

    # User does not exist
    # Hash the password and generate the session_id
    password_hash = hash_password(password)
    session_id = generate_session_id()

    # Create new user and insert
    new_user = Candidate(username = username, email = email, pass_hash = password_hash, session_id = str(session_id))
    new_user.insert_candidate()
    return jsonify({"status":"success", "username":username, "session_id":session_id})


#curl -X POST http://127.0.0.1:5000/api/login -d '{"username":"test","email":"test@gmail.com","password":"11111"}'  -H "Content-Type: application/json"
@app.route("/api/login", methods=["POST"])
def login():

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    print(Candidate.get_all_candidates())

    #query user
    user = Candidate.get_candidate(username)
    if user is None:
        return jsonify({"status": "fail", "message":"Account does not exist"})

    password_hash = hash_password(password)
    auth = verify_password(password, password_hash)

    if auth == True and username == user.username:
        session_id = str(generate_session_id())
        user.session_id = session_id
        user.update_candidate_info()
        return jsonify({"status":"success", "username":username, "session_id":session_id})
    return jsonify({"status":"fail"})


#curl -X POST http://127.0.0.1:5000/api/logout -d '{"session_id":"enter session_id here"}'  -H "Content-Type: application/json"
@app.route("/api/logout", methods=["POST"])
def logout():

    data = request.get_json()
    session_id = data.get("session_id")

    #query user with session_id
    # if user is None:
    #     return jsonify({"status":"logout failed"})

    #update session_id to None
    return jsonify({"status":"success"})

## Company Endpoints ##

# Get a list of all companies
# @app.route("/api/companies", methods=["GET"])

# Get a single company that matches the id
# @app.route("/api/companies/<company_id>", methods=["GET"])

# Add a company record
# @app.route("/api/companies/add", methods=["GET"])

# Update a company record
# @app.route("/api/companies/update", methods=["GET"])

# Delete a company record that matches the id
# @app.route("/api/companies/delete/<company_id>", methods=["GET"])


## Recruiter Endpoints ##

# Get a list of all recruiters
# @app.route("/api/recruiters", methods=["GET"])

# Get a single recruiter that matches the id
# @app.route("/api/recruiters/<recruiter_id>", methods=["GET"])

# Add a recruiter record
# @app.route("/api/recruiters/add", methods=["GET"])

# Update a recruiter record
# @app.route("/api/recruiters/update", methods=["GET"])

# Delete a recruiter record that matches the id
# @app.route("/api/recruiters/delete/<recruiter_id>", methods=["GET"])


## Candidate Endpoints ##

# Get a list of all candidates
# @app.route("/api/candidates", methods=["GET"])

# Get a single candidate that matches the id
# @app.route("/api/candidates/<candidate_id>", methods=["GET"])

# Add a candidate record
# @app.route("/api/candidates/add", methods=["POST"])

# Update a candidate record
# @app.route("/api/candidates/update", methods=["PUT"])

# Delete a candidate record that matches the id
# @app.route("/api/candidates/delete/<candidate_id>", methods=["DELETE"])


## Job Opening Endpoints ##

# Get a list of all job openings
# @app.route("/api/job-openings/", methods=["GET"])

# Get a single job opening that matches the id
# @app.route("/api/job-openings/<job_opening_id>", methods=["GET"])

# Add a job opening record
# @app.route("/api/job-openings/add", methods=["GET"])

# Update a job opening record
# @app.route("/api/job-openings/update", methods=["GET"])

# Delete a job opening record that matches the id
# @app.route("/api/job-openings/delete/<job_opening_id>", methods=["GET"])


## Application Endpoints ##

# Get a single application that matches the id
# @app.route("/api/applications/<application_id>", methods=["GET"])

# Add an application record
# @app.route("/api/applications/add", methods=["GET"])

# Update an application record
# @app.route("/api/applications/update", methods=["GET"])

# Delete an application record that matches the id
# @app.route("/api/applications/delete/<application_id>", methods=["GET"])

# Get all applications for a job given the job opening ID
# @app.route("/api/applications/<job_opening_id>", methods=["GET"])

# Get all applications for a candidate given the candidate ID
# @app.route("/api/applications/<job_opening_id>", methods=["GET"])

## Process Endpoints ##
# Get the process for a job given the job ID
# @app.route("/api/processes/", methods=["GET"])
