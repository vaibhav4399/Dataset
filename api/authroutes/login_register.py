from database.usermodel import users
from flask import make_response, jsonify, Blueprint, request
import json

login_register = Blueprint("login_register", __name__)

error = {
    "error": True,
    "message": "Invalid Credetials"
}


@login_register.route("/login/", methods=["POST"])
def login():
    body = request.get_json(force=True)
    if body.get("email") and body.get("password"):
        user = users.objects(email=body.get("email")).first()
        if user:
            if user.verify_password(body.get("password")):
                user = json.loads(user.to_json())
                user.pop("password")
                user["error"] = False
                return make_response(user, 200)
    return make_response(jsonify(error), 401)


@login_register.route("/register/", methods=["POST"])
def register():
    body = request.get_json(force=True)

    if body.get("name") and body.get("email") and body.get("password") and body.get("confirmpassword"):
        user = users.objects(email=body.get("email")).first()
        if not user:
            if body.get("password") == body.get("confirmpassword") and len(body.get("password")) >= 8:
                user = users(name=body.get("name"),
                             email=body.get("email"),
                             password=body.get("password"))
                user.password = user.hash_pass(user.password)
                user.save()
                user = json.loads(user.to_json())
                user.clear()
                user["error"] = False
                user["message"] = "OK"
                return make_response(user, 200)
            else:
                error["message"] = "Password does not match or less than 8 characters"
        else:
            error["message"] = "User exists"
    return make_response(jsonify(error), 400)
