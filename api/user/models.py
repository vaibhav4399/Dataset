from flask import jsonify, request, make_response
from config.connect import db


class User:

    def register(self):

        user = {
            "name": request.json.get("name"),
            "email": request.json.get("email"),
            "password": request.json.get("password")
        }

        return make_response(jsonify(user), 200)


db.users.insert_one({"name": "vaibhav"})
