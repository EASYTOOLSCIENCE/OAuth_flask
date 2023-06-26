from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "WELCOME TO EASYTOOL SCIENCE FIRST API"


@app.route("/register", methods=["POST"])
def register():

    if request.method == "POST":
        # Receive data

        # Register data into postgreSQL Database

        return {"created_user": "successfull"}

    return {"created_user": "failed"}


@app.route("/login", methods=["POST"])
def register():

    if request.method == "POST":
        # Receive data

        # Check and login user from postgreSQL Database

        return {"logged_user": "successfull"}

    return {"logged_user": "failed"}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
