# app/modules/auth/service.py
from app.utils.weixin import WeixinAPI
from app.utils.crypto import decrypt_data
import jwt
import datetime


class AuthService:
    @staticmethod
    def login(code):
        result = WeixinAPI.code2session(code)
        access_token = WeixinAPI.get_access_token()
        if "errcode" in result:
            raise Exception(f"Login failed: {result.get('errmsg')}")

        openid = result["openid"]
        session_key = result["session_key"]

        # 生成 JWT
        payload = {
            "openid": openid,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }
        token = jwt.encode(payload, "your_jwt_secret", algorithm="HS256")
        return {"token": token, "openid": openid, "access_token": access_token, "session_key": session_key}

    @staticmethod
    def get_phone_number(encrypted_data, iv, session_key):
        try:
            phone_data = decrypt_data(encrypted_data, iv, session_key)
            return phone_data.get("phoneNumber")
        except Exception as e:
            raise Exception(f"Decrypt failed: {str(e)}")