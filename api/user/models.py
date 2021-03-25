from flask import jsonify, request, make_response
from config.connect import db
from bson import json_util
import json


class User:

    error = {
        "error": True
    }

    def register(self):

        if request.json.get("name") and request.json.get("email") and request.json.get("password"):
            user = {
                "name": request.json.get("name"),
                "email": request.json.get("email"),
                "password": request.json.get("password")
            }

            if db.users.find_one({"email": user["email"]}):

                self.error["message"] = "User already exists!"

                return make_response(jsonify(self.error), 403)

            else:
                insert = db.users.insert_one(user)
                user["error"] = False
                new = json.loads(json_util.dumps(user))
                return make_response(jsonify(new), 200)

        else:

            self.error["message"] = "Invalid details"

            return make_response(jsonify(self.error), 400)

    def login(self):

        if request.json.get("email") and request.json.get("password"):

            result = db.users.find_one({"email": request.json.get("email")})

            if result:
                if result["password"] == request.json.get("password"):
                    user = json.loads(json_util.dumps(result))
                    user["error"] = False
                    return make_response(jsonify(user), 200)
                else:
                    self.error["message"] = "Invalid Credentials"
                    return make_response(jsonify(self.error), 402)

            else:
                self.error["message"] = "User does not exists!"
                return make_response(jsonify(self.error), 402)

        else:
            self.error["message"] = "Invalid Details!"
            return make_response(jsonify(self.error), 400)
