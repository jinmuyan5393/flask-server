# app/modules/auth/routes.py
from flask import Blueprint, request, jsonify
from .service import AuthService

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    code = data.get("code")
    if not code:
        return jsonify({"error": "Code is required"}), 400

    try:
        result = AuthService.login(code)
        return jsonify({"data": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@auth_bp.route("/phone", methods=["POST"])
def get_phone():
    data = request.json
    encrypted_data = data.get("encryptedData")
    iv = data.get("iv")
    session_key = data.get("session_key")

    if not all([encrypted_data, iv, session_key]):
        return jsonify({"error": "Missing parameters"}), 400

    try:
        phone = AuthService.get_phone_number(encrypted_data, iv, session_key)
        return jsonify({"data": {"phone": phone}}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500