from flask import make_response, jsonify, Blueprint
from user.models import User


user = Blueprint("user", __name__)


@user.route("/login/", methods=["POST"])
def login():
    return User().login()


@user.route("/signup/", methods=["POST"])
def signup():

    return User().register()


@user.route("/croppredict/")
def croppredict():
    pass
