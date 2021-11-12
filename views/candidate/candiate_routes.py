from flask import request, jsonify
from models.utils import hash_password, verify_password, generate_session_id
from models.schemas.candidate import Candidate

def list_candidates():
    candidates = Candidate.get()
    if candidates:
        return jsonify({"message":"success", "candidates":candidates})
    return jsonify({"message":"Candidate does not exists."})

def get_candidate_by_id(candidate_id):
    candidate = Candidate.get_candidate("candidate_id", candidate_id)
    if candidate and candidate.first_name and candidate.last_name:
        return jsonify({"message":"success", "candidate":{"id":candidate.id, "first_name":candidate.first_name,"last_name":candidate.last_name, "email":candidate.email,"phone":candidate.phone, "description":candidate.description}})
    return jsonify({"message":"Candidate does not exists."})


def mutate_candidate_record():
    data = request.get_json()
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    phone = data.get("phone")
    description = data.get("description")
    session_id = data.get("session_id")

    candidate = Candidate.get("session_id", session_id)
    if candidate is None:
        return jsonify({"Status":"fail"})
    if first_name:
        candidate.first_name = first_name
    if last_name:
        candidate.last_name = last_name
    if email:
        candidate.email = email
    if phone:
        candidate.phone = phone
    if description:
        candidate.description = description
    candidate.update_candidate()
    return jsonify({"status":"success"})

def delete_candiate_record(id):
    candidate = Candidate.get_candidate("candidate_id", id)
    if candidate is None:
        return jsonify({"status":"fail", "message":"This candidate does not exits."})
    candidate.delete_candidate(id)
    return jsonify({"status":"success"})
