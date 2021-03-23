from flask import Flask, make_response, jsonify
from user.routes import user
from flask_cors import CORS

app = Flask(__name__)
app.url_map.strict_slashes = False

cors = CORS(app)


app.register_blueprint(user, url_prefix="/user")

if __name__ == "__main__":
    app.run(debug="True")
