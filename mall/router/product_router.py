# -*- encoding : utf-8 -*-
"""
@File       : product_router.py
@Time       :2021/1/22 17:24
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
from flask import Blueprint

from mall.db.models.product import product_api

app_product = Blueprint('product', __name__)


@app_product.route('/list')
def get_product_list():
    result = product_api.get_product_list()
    return result


