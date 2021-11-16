from flask import request, jsonify
from models.classes.experience import Experience

def list_experiences():
    experiences = Experience.get_all()
    if experiences:
        return jsonify({"status":"success", "experiences":experiences})
    return jsonify({"status":"fail", "message":"No experiences in database."})  #added status to use in frontend

def insert_experience():
    data = request.get_json()
    candidate_id = data.get("candidate_id")
    college_id = data.get("college_id")
    date_start = data.get("date_start")
    date_end = data.get("date_end")
    description = data.get("description")

    # Optional: Query database to see if the job opening already exists

    new_experience = Experience(candidate_id = candidate_id, college_id = college_id, degree_id = degree_id, date_start = date_start, date_end = date_end, description = description)
    new_experience.insert()

    return jsonify({"status":"success"})

def get_experience(experience_id):
    experience = Experience.get(experience_id)
    if experience:
        return jsonify(
            {
                "message":"success",
                "experience":{
                    "id":experience.id,
                    "candidate_id":experience.candidate_id,
                    "college_id":experience.college_id,
                    "degree_id":experience.degree_id,
                    "date_start":experience.date_start,
                    "date_end":experience.date_end,
                    "description":experience.description
                }
            }
        )
    return jsonify({"status":"fail","message":"Experience does not exists."})

def update_experience():
    data = request.get_json()
    id = data.get("id")
    candidate_id = data.get("candidate_id")
    college_id = data.get("college_id")
    date_start = data.get("date_start")
    date_end = data.get("date_end")
    description = data.get("description")

    experience = Experience.get(id)
    if experience is None:
        return jsonify({"status":"fail"})
    if candidate_id:
        experience.candidate_id = candidate_id
    if college_id:
        experience.college_id = college_id
    if date_start:
        experience.date_start = date_start
    if date_end:
        experience.date_end = date_end
    if description:
        experience.description = description
    experience.update()
    return jsonify({"status":"success"})

def delete_experience(experience_id):
    experience = Experience.get("id", experience_id)
    if experience:
        Experience.delete(experience_id)
        jsonify({"status":"success"})
    return jsonify({"status":"fail"})
