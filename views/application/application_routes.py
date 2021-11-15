from flask import request, jsonify
from models.classes.application import Application

def list_applications():
    applications = Application.get_all()
    if applications:
        return jsonify({"status":"success", "applications":applications})
    return jsonify({"status":"fail", "message":"No applications in database."})  #added status to use in frontend

def insert_application():
    data = request.get_json()
    date_of_application = data.get("date_of_application")
    job_opening_id = data.get("job_opening_id")
    candidate_id = data.get("candidate_id")
    status = data.get("status")

    # Optional: Query database to see if the job opening already exists

    new_application = Application(date_of_application=date_of_application,job_opening_id=job_opening_id,candidate_id=candidate_id,status=status)
    new_application.insert()

    return jsonify({"status":"success"})

def get_application(application_id):
    application = Application.get(application_id)
    if application:
        return jsonify(
            {
                "message":"success",
                "application":{
                    "id":application.id,
                    "date_of_application":application.date_of_application,
                    "job_opening_id":application.job_opening_id,
                    "candidate_id":application.candidate_id,
                    "status":application.status
                }
            }
        )
    return jsonify({"status":"fail","message":"Application does not exists."})

def update_application():
    data = request.get_json()
    id = data.get("id")
    date_of_application = data.get("date_of_application")
    job_opening_id = data.get("job_opening_id")
    candidate_id = data.get("candidate_id")
    status = data.get("status")

    application = Application.get(id)
    if application is None:
        return jsonify({"status":"fail"})
    if date_of_application:
        application.date_of_application = date_of_application
    if job_opening_id:
        application.job_opening_id = job_opening_id
    if candidate_id:
        application.candidate_id = candidate_id
    if status:
        application.status = status
    application.update()
    return jsonify({"status":"success"})

def delete_application(application_id):
    application = Application.get("id", application_id)
    if application:
        Application.delete(application_id)
        jsonify({"status":"success"})
    return jsonify({"status":"fail"})
