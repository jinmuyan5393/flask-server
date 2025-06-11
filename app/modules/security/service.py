# app/modules/security/service.py
from app.utils.weixin import WeixinAPI
import requests

class SecurityService:
    @staticmethod
    def check_text(content):
        access_token = "your_access_token"  # 需实现获取 access_token 的逻辑
        url = f"{WeixinAPI.BASE_URL}/wxa/msg_sec_check?access_token={access_token}"
        data = {"content": content}
        response = requests.post(url, json=data)
        result = response.json()
        if result.get("errcode") != 0:
            raise Exception(f"Check failed: {result.get('errmsg')}")
        return result