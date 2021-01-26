# -*- encoding : utf-8 -*-
"""
@File       : product_inner_func.py
@Time       :2021/1/26 19:53
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

from mall.db.models.product import product_dao as ProductAPI

from mall.common.common import deco_catch_func_exception


@deco_catch_func_exception("获取商品")
def get_product():
    plist = ProductAPI.get_product_list()
    return plist
