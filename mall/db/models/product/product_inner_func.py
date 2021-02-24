# -*- encoding : utf-8 -*-
"""
@File       : product_inner_func.py
@Time       :2021/1/26 19:53
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
from mall.db.engines.mysql import get_session
from mall.db.models.product import product_dao as ProductAPI


def get_product():
    session = get_session()
    plist = ProductAPI.get_product_list(session)
    return plist
