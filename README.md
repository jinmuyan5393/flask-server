# flask-server
基于Flask的后端restful api

weixin_mini_sdk/
├── app/ # 核心应用代码
│ ├── init.py # Flask 应用初始化
│ ├── config/ # 配置文件
│ │ ├── init.py
│ │ ├── base.py # 基础配置
│ │ └── dev.py # 开发环境配置
│ ├── modules/ # 功能模块
│ │ ├── init.py
│ │ ├── auth/ # 认证相关（登录、手机号授权）
│ │ │ ├── init.py
│ │ │ ├── routes.py # API 路由
│ │ │ └── service.py # 业务逻辑
│ │ ├── message/ # 消息相关（模板消息、客服消息）
│ │ │ ├── init.py
│ │ │ ├── routes.py
│ │ │ └── service.py
│ │ ├── security/ # 内容安全检测
│ │ │ ├── init.py
│ │ │ ├── routes.py
│ │ │ └── service.py
│ │ └── future/ # 预留扩展模块（如 AI、支付）
│ │ ├── init.py
│ │ └── placeholder.py
│ ├── utils/ # 工具函数
│ │ ├── init.py
│ │ ├── weixin.py # 微信 API 封装
│ │ ├── crypto.py # 加密解密工具
│ │ └── logger.py # 日志工具
│ └── middleware/ # 中间件
│ ├── init.py
│ └── auth.py # API 鉴权中间件
├── tests/ # 单元测试
│ ├── init.py
│ └── test_auth.py
├── requirements.txt # 依赖文件
├── run.py # 启动脚本
├── README.md # 项目说明
└── .env # 环境变量