# app/__init__.py
from flask import Flask
from .config.base import DevConfig
from .modules.auth.routes import auth_bp
from .modules.message.routes import message_bp
from .modules.security.routes import security_bp

def create_app(config_class=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 注册蓝图
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(message_bp, url_prefix="/api/message")
    app.register_blueprint(security_bp, url_prefix="/api/security")

    return app