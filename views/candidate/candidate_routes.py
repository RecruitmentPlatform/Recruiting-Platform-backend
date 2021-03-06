from flask import request, jsonify
from models.classes.candidate import Candidate

def list_candidates(table_name):
    candidates = Candidate.get_all(table_name)
    if candidates:
        return jsonify({"status":"success", "candidates":candidates})
    return jsonify({"status":"fail", "message":"No candidates in database."})  #added status to use in frontend

def get_candidate(candidate_id, criteria="id"):
    candidate = Candidate.get(criteria, candidate_id)
    if candidate:
        return jsonify(
            {
                "message":"success",
                "candidate":{
                    "id":candidate.id,
                    "first_name":candidate.first_name,
                    "last_name":candidate.last_name,
                    "email":candidate.email,
                    "phone":candidate.phone,
                    "description":candidate.description,
                    "ethnicity_id":candidate.ethnicity_id,
                    "gender_id":candidate.gender_id,
                    "gender_pronoun_id":candidate.gender_pronoun_id
                }
            }
        )
    return jsonify({"status":"fail","message":"Candidate does not exists."})

def update_candidate():
    data = request.get_json()
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    phone = data.get("phone")
    description = data.get("description")
    session_id = data.get("session_id")
    ethnicity_id = data.get("ethnicity_id")
    gender_id = data.get("gender_id")
    gender_pronoun_id= data.get("gender_pronoun_id")

    candidate = Candidate.get("session_id", session_id)
    if candidate is None:
        return jsonify({"status":"fail"})
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
    if ethnicity_id:
        candidate.ethnicity_id = ethnicity_id
    if gender_id:
        candidate.gender_id = gender_id
    if gender_pronoun_id:
        candidate.gender_pronoun_id = gender_pronoun_id
    candidate.update()
    return jsonify({"status":"success"})

def delete_candidate(candidate_id):
    candidate = Candidate.get("id", candidate_id)
    if candidate:
        Candidate.delete(candidate_id)
        jsonify({"status":"success"})
    return jsonify({"status":"fail"})
