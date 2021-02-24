# -*- encoding : utf-8 -*-
"""
@File       : engineTest.py
@Time       :2021/1/27 9:38
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

from oslo_db.sqlalchemy import enginefacade
from mall.db.models.product.product_model import Product


class MyContext:
    pass


def reader(context):
    with enginefacade.reader.using(context) as session:
        return session.query(Product).all()
