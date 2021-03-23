from flask import jsonify, request, make_response
from config.connect import db
from bson import json_util
import json


class User:

    def register(self):

        if request.json.get("name") and request.json.get("email") and request.json.get("password"):
            user = {
                "name": request.json.get("name"),
                "email": request.json.get("email"),
                "password": request.json.get("password")
            }

            if db.users.find_one({"email": user["email"]}):
                error = {
                    "error": True,
                    "message": "User Already Exists!"
                }
                return make_response(jsonify(error), 403)

            else:
                db.users.insert_one(user)
                user["error"] = False
                new = json.loads(json_util.dumps(user))
                return make_response(jsonify(new), 200)

        else:
            error = {
                "error": True,
                "message": "User Already Exists!"
            }
            return make_response(jsonify(error), 400)
