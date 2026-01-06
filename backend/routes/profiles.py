from flask import Blueprint, request, jsonify
from db import users

profiles_bp = Blueprint("profiles", __name__, url_prefix="/profiles")

@profiles_bp.route("/create", methods=["POST"])
def create_profile():
    data = request.json

    if "user_type" not in data or "name" not in data:
        return jsonify({"error": "user_type and name required"}), 400

    users.insert_one(data)
    return jsonify({"message": "Profile created"}), 201


@profiles_bp.route("/<user_type>", methods=["GET"])
def get_profiles(user_type):
    profiles = list(users.find({"user_type": user_type}, {"_id": 0}))
    return jsonify(profiles)
