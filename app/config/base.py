# app/config/base.py
import os
from dotenv import load_dotenv

load_dotenv()

class BaseConfig:
    WEIXIN_APP_ID = os.getenv("WEIXIN_APP_ID")
    WEIXIN_APP_SECRET = os.getenv("WEIXIN_APP_SECRET")
    DEBUG = False

class DevConfig(BaseConfig):
    DEBUG = True