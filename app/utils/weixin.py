# app/utils/weixin.py
import requests
from flask import current_app
import time

class WeixinAPI:
    BASE_URL = "https://api.weixin.qq.com"
    _access_token = None
    _access_token_expiry = 0

    @staticmethod
    def get_access_token():
        """获取 access_token，优先从缓存读取"""
        current_time = time.time()

        # 检查缓存
        if WeixinAPI._access_token and current_time < WeixinAPI._access_token_expiry:
            return WeixinAPI._access_token

        # 请求微信 API
        url = f"{WeixinAPI.BASE_URL}/cgi-bin/token"
        params = {
            "grant_type": "client_credential",
            "appid": current_app.config["WEIXIN_APP_ID"],
            "secret": current_app.config["WEIXIN_APP_SECRET"]
        }
        response = requests.get(url, params=params)
        result = response.json()

        if "errcode" in result:
            raise Exception(f"Failed to get access_token: {result.get('errmsg')}")

        WeixinAPI._access_token = result["access_token"]
        # 设置过期时间，提前 60 秒刷新以避免边界问题
        WeixinAPI._access_token_expiry = current_time + result["expires_in"] - 60
        return WeixinAPI._access_token

    @staticmethod
    def code2session(code):
        url = f"{WeixinAPI.BASE_URL}/sns/jscode2session"
        params = {
            "appid": current_app.config["WEIXIN_APP_ID"],
            "secret": current_app.config["WEIXIN_APP_SECRET"],
            "js_code": code,
            "grant_type": "authorization_code"
        }
        print("params: ", params)
        response = requests.get(url, params=params)
        return response.json()

    @staticmethod
    def send_template_message(access_token, data):
        url = f"{WeixinAPI.BASE_URL}/cgi-bin/message/wxopen/template/send?access_token={access_token}"
        response = requests.post(url, json=data)
        return response.json()