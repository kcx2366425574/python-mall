# -*- encoding : utf-8 -*-
"""
@File       : product_dao.py
@Time       :2021/1/26 19:18
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

from mall.db.engines.mysql import get_session
from mall.db.models.product.product_model import Product


def get_product_list(session):
    with session.begin():
        plist = session.query(Product).all()
        return plist
