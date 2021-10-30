from flask import Flask, request, jsonify
from flask_cors import CORS

# from models.settings import session
from models.utils import hash_password, verify_password, generate_session_id



app = Flask(__name__)
CORS(app)


#curl -X POST http://127.0.0.1:5000/api/signup -d '{"username":"test","email":"test@gmail.com","password":"11111"}'  -H "Content-Type: application/json"
@app.route("/api/signup", methods=["POST"])  
def signup():

    data = request.get_json()
    print(data)
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    password_hash = hash_password(password)
    session_id = generate_session_id()

    #query user here
    #if user already exists
    #     return jsonify({"status":"fail", "message":"Account already exists"})

    #otherwise insert user info into user table

    return jsonify({"status":"success", "username":username, "session_id":session_id})


#curl -X POST http://127.0.0.1:5000/api/login -d '{"username":"test","email":"test@gmail.com","password":"11111"}'  -H "Content-Type: application/json"
@app.route("/api/login", methods=["POST"])
def login():
    
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    #query user 
    # if user is None:
    #     return jsonify({"status": "fail", "message":"account does not exist"})
    #otherwise
    uname = "test"

    password_hash = hash_password(password)
    auth = verify_password(password, password_hash)
    if auth == True and username == uname:
        session_id = str(generate_session_id())
        #store session_is
        return jsonify({"status":"success", "username":username, "session_id":session_id})
    return jsonify({"status":"fail"})

#curl -X POST http://127.0.0.1:5000/api/logout -d '{"session_id":"enter session_id here"}'  -H "Content-Type: application/json"
@app.route("/api/logout", methods=["POST"])
def logout():

    data = request.get_json()
    session_id = data.get("session_id")

    #query user with session_id
    # if user is None:
    #     return jsonify({"status":"logout failed"})

    #update session_id to None
    return jsonify({"status":"success"})