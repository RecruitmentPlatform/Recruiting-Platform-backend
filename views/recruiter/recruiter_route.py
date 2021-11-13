from flask import request, jsonify
from models.utils import hash_password, verify_password, generate_session_id
from models.classes.recruiter import Recruiter

def insert_recruiters():
    data = request.get_json()

def all_recruiters():
    #rtype -> list of tuples
    #convert it to a list of hashmaps
    recruiters = Recruiter.get_all_recruiters()
    print(recruiters)

def get_a_recruiter():
    data = request.get_json()
    id = data.get("id")
    recruiter = Recruiter.get_recruiter_by_id(id)
    if recruiter is None:
        return jsonify({"status":"fail", "message":"This recruiter does not exists."})
    return jsonify({"status":"success", "recruiter":recruiter})
