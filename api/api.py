from flask import Flask
from views import blue
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app)

app.register_blueprint(blue,url_prefix="/")

if __name__ == "__main__":
	app.run(debug="True")
