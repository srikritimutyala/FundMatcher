from flask import Blueprint, jsonify
from db import users
from services.matcher import compatibility_score

match_bp = Blueprint("match", __name__, url_prefix="/match")

@match_bp.route("/founder/<name>", methods=["GET"])
def match_founder(name):
    founder = users.find_one(
        {"name": name, "user_type": "founder"},
        {"_id": 0}
    )

    if not founder:
        return jsonify({"error": "Founder not found"}), 404

    investors = list(users.find(
        {"user_type": "investor"},
        {"_id": 0}
    ))

    results = []
    for investor in investors:
        score = compatibility_score(founder, investor)
        results.append({
            "investor": investor["name"],
            "score": score
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return jsonify(results)
