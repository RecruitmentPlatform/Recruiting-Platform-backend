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

def get_job_opening(job_opening_id):
    job_opening = JobOpening.get(job_opening_id)
    if job_opening:
        return jsonify(
            {
                "message":"success",
                "job_opening":{
                    "id":job_opening.id,
                    "name":job_opening.name,
                    "description":job_opening.description,
                    "date_published":job_opening.date_published,
                    "date_deadline":job_opening.date_deadline,
                    "date_start_job":job_opening.date_start_job,
                    "vacancy_count":job_opening.vacancy_count,
                    "job_category_id":job_opening.job_category_id,
                    "job_position_id":job_opening.job_position_id,
                    "company_id":job_opening.company_id,
                    "recruiter_id":job_opening.recruiter_id
                }
            }
        )
    return jsonify({"message":"Job opening does not exists."})
