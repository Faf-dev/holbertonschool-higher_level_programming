#!/usr/bin/python3
"""
Create a simple API with authentification
"""
from flask import Flask
from flask import jsonify
from flask import request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import create_access_token

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)


users = {
    "user1":
    {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
        },
    "admin1":
    {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
        }
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)

    if user:
        if check_password_hash(user['password'], password):
            return user

    return None


@app.route('/basic-protected', methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route('/login', methods=["POST"])
def login():
    data = request.get_json()

    if not data or "username" not in data or "password"not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data.get("username")
    password = data.get("password")

    if username in users and \
            check_password_hash(users[username]["password"], password):
        token = create_access_token(identity=username)
        return jsonify({"access_token": token}), 200

    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected', methods=["GET"])
@jwt_required()
def protected():
    return "JWT Auth: Access Granted", 200


@app.route('/admin-only', methods=["GET"])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    user_info = users.get(current_user)

    if not user_info or user_info["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted", 200


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
