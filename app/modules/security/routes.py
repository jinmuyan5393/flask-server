# app/modules/security/routes.py
from flask import Blueprint, request, jsonify
from .service import SecurityService

security_bp = Blueprint("security", __name__)


@security_bp.route("/text_check", methods=["POST"])
def check_text():
    data = request.json
    content = data.get("content")

    if not content:
        return jsonify({"error": "Content is required"}), 400

    try:
        result = SecurityService.check_text(content)
        return jsonify({"data": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500