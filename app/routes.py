from app import app
from flask import render_template, jsonify


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html")
@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")










# APIs
#dummy
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]
@app.route("/api/users", methods=['GET', 'POST'])
def get_users():
    #dummy for now
    return jsonify(users)

@app.route("/api/users/<int:id>", methods=['GET', 'POST'])
def get_user(id):
    for user in users:
        if user["id"] == id:
            return jsonify(user)
    
    