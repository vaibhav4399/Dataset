from flask import request, jsonify, Blueprint, make_response
blue = Blueprint('blueprint', __name__)


@blue.route("/")
def index():
	return make_response(jsonify(),200)

@blue.route("/about")
def about():
	#abort(200)
	return make_response(jsonify(),500)

@blue.route("/home")
def home():
	return make_response(jsonify(message="home section",hi="hi",sor="sor"),404)


@blue.route("/contact")
def contact():
	return make_response(jsonify(message="contacts"),200)


@blue.route("/predict", methods=["POST","GET"])
def predict():
	if request.method == "POST":
		return make_response(jsonify(message="Predictions"),200)
	else:
		return make_response(jsonify(error="error"),422)
