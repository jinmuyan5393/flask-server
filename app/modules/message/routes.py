# app/modules/message/routes.py
from flask import Blueprint, request, jsonify
from .service import MessageService

message_bp = Blueprint("message", __name__)


@message_bp.route("/template", methods=["POST"])
def send_template():
    data = request.json
    openid = data.get("openid")
    template_id = data.get("template_id")
    template_data = data.get("data")
    page = data.get("page")

    if not all([openid, template_id, template_data]):
        return jsonify({"error": "Missing parameters"}), 400

    try:
        result = MessageService.send_template_message(openid, template_id, template_data, page)
        return jsonify({"data": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500