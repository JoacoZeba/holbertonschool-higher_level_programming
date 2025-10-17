import json
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory data store for users
users = {}

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"

@app.route("/status", methods=["GET"])
def get_status():
    return "OK"

@app.route("/data", methods=["GET"])
def get_usernames():
    return jsonify(list(users.keys()))

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user_data = users.get(username)
    if user_data:
        return jsonify(user_data)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        user_data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if not user_data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = user_data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    user_data["username"] = username
    users[username] = user_data

    response = {
        "message": "User added",
        "user": user_data
    }
    return jsonify(response), 201

if __name__ == "__main__":
    app.run(debug=True)
