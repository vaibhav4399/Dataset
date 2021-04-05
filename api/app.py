from flask import Flask
from flask_cors import CORS
from authroutes.login_register import login_register


app = Flask(__name__)
cors = CORS(app)


app.url_map.strict_slashes = False

app.register_blueprint(login_register, url_prefix="/auth")

if __name__ == '__main__':
    app.run()
