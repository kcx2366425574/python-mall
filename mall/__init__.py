# -*- encoding : utf-8 -*-
"""
@File       : __init__.py.py
@Time       :2021/1/22 10:37
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
from flask import Flask
from flask_cors import CORS

from mall.router import app_test
from mall.router.product_router import app_product


app = Flask(__name__)
CORS(app)

# 注册组件
app.register_blueprint(app_product, url_prefix="/product")
app.register_blueprint(app_test, url_prefix="/")
