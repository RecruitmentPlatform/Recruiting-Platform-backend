from flask import request, jsonify
from models.classes.education import Education

def list_educations():
    educations = Education.get_all()
    if educations:
        return jsonify({"status":"success", "educations":educations})
    return jsonify({"status":"fail", "message":"No educations in database."})  #added status to use in frontend

def insert_education():
    data = request.get_json()
    candidate_id = data.get("candidate_id")
    college_id = data.get("college_id")
    date_start = data.get("date_start")
    date_end = data.get("date_end")
    description = data.get("description")

    # Optional: Query database to see if the job opening already exists

    new_education = Education(candidate_id = candidate_id, college_id = college_id, degree_id = degree_id, date_start = date_start, date_end = date_end, description = description)
    new_education.insert()

    return jsonify({"status":"success"})

def get_education(education_id):
    education = Education.get(education_id)
    if education:
        return jsonify(
            {
                "message":"success",
                "education":{
                    "id":education.id,
                    "candidate_id":education.candidate_id,
                    "college_id":education.college_id,
                    "degree_id":education.degree_id,
                    "date_start":education.date_start,
                    "date_end":education.date_end,
                    "description":education.description
                }
            }
        )
    return jsonify({"status":"fail","message":"Education does not exists."})

def update_education():
    data = request.get_json()
    id = data.get("id")
    candidate_id = data.get("candidate_id")
    college_id = data.get("college_id")
    date_start = data.get("date_start")
    date_end = data.get("date_end")
    description = data.get("description")

    education = Education.get(id)
    if education is None:
        return jsonify({"status":"fail"})
    if candidate_id:
        education.candidate_id = candidate_id
    if college_id:
        education.college_id = college_id
    if date_start:
        education.date_start = date_start
    if date_end:
        education.date_end = date_end
    if description:
        education.description = description
    education.update()
    return jsonify({"status":"success"})

def delete_education(education_id):
    education = Education.get("id", education_id)
    if education:
        Education.delete(education_id)
        jsonify({"status":"success"})
    return jsonify({"status":"fail"})
