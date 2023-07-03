from flask import Flask, request
import authModel

app = Flask(__name__)


@app.route("/")
def home():
    return "WELCOME TO EASYTOOL SCIENCE FIRST API"


@app.route("/register", methods=["POST"])
def register():

    if request.method == "POST":
        # Receive data
        name = request.form.get("name")
        password = request.form.get("password")
        # Register data into postgreSQL Database
        response = authModel.create(name, password)
        return {"created_user": "successfull"}

    return {"created_user": "failed"}


@app.route("/login", methods=["POST"])
def login():

    if request.method == "POST":
        # Receive data
        name = request.form.get("name")
        password = request.form.get("password")

        # Check and login user from postgreSQL Database
        user = authModel.login(name, password)
        return {"logged_user": user}

    return {"logged_user": "failed"}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
