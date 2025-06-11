# app/middleware/auth.py
from flask import request, jsonify
import jwt

def require_auth(f):
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Token is required"}), 401
        try:
            jwt.decode(token, "your_jwt_secret", algorithms=["HS256"])
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
        return f(*args, **kwargs)
    return decorated