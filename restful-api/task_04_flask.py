#!/usr/bin/python3
"""
Create a simple API
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    if not username:
        return jsonify({"error": "User already exist!"}), 400
    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({"message": "Success, user added !", "user": data}), 201


if __name__ == "__main__":
    app.run()
