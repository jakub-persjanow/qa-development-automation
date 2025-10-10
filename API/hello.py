from flask import Flask, abort

users = [
    {"fname": "Jakub",
    "lname": "Persjanow"},
    {"fname": "Demian",
    "lname": "Gela"}
]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello!</p>"

@app.get("/users")
def show_users():
    # abort(404)
    return users
