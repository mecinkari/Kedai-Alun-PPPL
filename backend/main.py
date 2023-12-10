from flask import Flask, jsonify, request
from flask_cors import CORS
from routes.user import user
from routes.auth import auth
from routes.api import api

app = Flask(__name__)
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(api, url_prefix="/api")
CORS(app, origins=["http://127.0.0.1:1010", "http://localhost:5173"])


@app.route("/", methods=["GET"])
def index():
    return {"msg": "Hi! 👋"}


if __name__ == "__main__":
    app.run(debug=True, port=1010)
