# -*- encoding : utf-8 -*-
"""
@File       : product_api.py
@Time       :2021/1/26 20:31
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

from mall.common.common import deco_catch_view_exception

from mall.db.models.product import product_inner_func as ProductIN


@deco_catch_view_exception("获取商品")
def get_product_list():
    product_list = ProductIN.get_product()
