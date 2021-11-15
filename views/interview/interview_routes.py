from flask import request, jsonify
from models.classes.interview import Interview

def list_interviews():
    interviews = Interview.get_all()
    if interviews:
        return jsonify({"status":"success", "interviews":interviews})
    return jsonify({"status":"fail", "message":"No interviews in database."})  #added status to use in frontend

def insert_interview():
    data = request.get_json()
    application_id = data.get("application_id")
    date_start = data.get("date_start")
    date_end = data.get("date_end")
    status = data.get("status")

    # Optional: Query database to see if the job opening already exists

    new_interview = Interview(application_id=application_id,date_start=date_start,date_end=date_end,status=status)
    new_interview.insert()

    return jsonify({"status":"success"})

def get_interview(interview_id):
    interview = Interview.get(interview_id)
    if interview:
        return jsonify(
            {
                "message":"success",
                "interview":{
                    "id":interview.id,
                    "application_id":interview.application_id,
                    "date_start":interview.date_start,
                    "date_end":interview.date_end,
                    "status":interview.status
                }
            }
        )
    return jsonify({"status":"fail","message":"Interview does not exists."})

def update_interview():
    data = request.get_json()
    id = data.get("id")
    date_of_interview = data.get("application_id")
    job_opening_id = data.get("date_start")
    candidate_id = data.get("date_end")
    status = data.get("status")

    interview = Interview.get(id)
    if interview is None:
        return jsonify({"status":"fail"})
    if application_id:
        interview.application_id = application_id
    if date_start:
        interview.date_start = date_start
    if date_end:
        interview.date_end = date_end
    if status:
        interview.status = status
    interview.update()
    return jsonify({"status":"success"})

def delete_interview(interview_id):
    interview = Interview.get("id", interview_id)
    if interview:
        Interview.delete(interview_id)
        jsonify({"status":"success"})
    return jsonify({"status":"fail"})
