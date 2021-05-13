# -*- encoding : utf-8 -*-
"""
@File       : __init__.py.py
@Time       :2021/1/22 14:20
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
from flask import Blueprint

app_test = Blueprint('test', __name__)


@app_test.route('/metrics', methods=['GET'])
def index():
    a = "# HELP node_custome_data creates by kuangcx\n"
    a += "# TYPE node_custome_data gauge\n"
    a += "node_custome_data 0620\n"
    return a


