from flask import request, jsonify

from models.utils import hash_password, verify_password, generate_session_id

from models.classes.candidate import Candidate


def signup_user():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    # Query database to see if user already exists
    user = Candidate.get("email", email)
    if user:
        return jsonify({"status":"fail", "message":"This account already exists."})

    # User does not exist
    # Hash the password and generate the session_id
    password_hash = hash_password(password)
    session_id = generate_session_id()

    new_user = Candidate(email = email, pass_hash = password_hash, session_id = str(session_id))
    new_user.insert()
    return jsonify({"status":"success",  "session_id":session_id})


def login_user():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    #query user
    user = Candidate.get("email",email)
    if user is None:
        return jsonify({"status": "fail", "message":"Account does not exist"})

    password_hash = hash_password(password)
    auth = verify_password(password, password_hash)

    if auth == True and email == user.email:
        session_id = str(generate_session_id())
        user.session_id = session_id
        user.update()
        return jsonify({"status":"success", "session_id":session_id})
    return jsonify({"status":"fail", "message":"Login failed."})

def logout_user():
    data = request.get_json()
    session_id = data.get("session_id")

    #query user with session_id
    user = Candidate.get("session_id", session_id)

    if user is None:
        return jsonify({"status":"logout failed"})

    user.session_id = None
    user.update()
    return jsonify({"status":"success"})
