from flask import Flask, make_response, jsonify
from user.routes import user
from flask_cors import CORS

app = Flask(__name__)
app.url_map.strict_slashes = False

cors = CORS(app)


@app.route("/")
def home():
    return make_response(jsonify(message="Hello"), 200)


@app.route("/about/")
def about():
    return make_response(jsonify(message="about"), 200)


@app.route("/contact/")
def contact():
    return make_response(jsonify(message="contacts"), 200)


app.register_blueprint(user, url_prefix="/user")

if __name__ == "__main__":
    app.run(debug="True")
