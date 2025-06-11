# app/modules/message/service.py
from app.utils.weixin import WeixinAPI

class MessageService:
    @staticmethod
    def send_template_message(openid, template_id, data, page=None):
        access_token = "your_access_token"  # 需实现获取 access_token 的逻辑
        message_data = {
            "touser": openid,
            "template_id": template_id,
            "page": page,
            "data": data
        }
        result = WeixinAPI.send_template_message(access_token, message_data)
        if "errcode" in result and result["errcode"] != 0:
            raise Exception(f"Send failed: {result.get('errmsg')}")
        return result