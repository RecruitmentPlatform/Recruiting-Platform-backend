from flask import request, jsonify

from models.classes.job_opening import JobOpening

def insert_job_opening():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    date_published = data.get("date_published")
    date_deadline = data.get("date_deadline")
    date_start_job = data.get("date_start_job")
    vacancy_count = data.get("vacancy_count")
    job_category_id = data.get("job_category_id")
    job_position_id = data.get("job_position_id")
    company_id = data.get("company_id")
    recruiter_id = data.get("recruiter_id")

    # Optional: Query database to see if the job opening already exists

    new_job_opening = JobOpening(name=name,description=description,date_published=date_published,date_deadline=date_deadline,date_start_job=date_start_job,vacancy_count=vacancy_count,job_category_id=job_category_id,job_position_id=job_position_id,company_id=company_id,recruiter_id=recruiter_id)
    new_job_opening.insert()

    return jsonify({"status":"success"})
