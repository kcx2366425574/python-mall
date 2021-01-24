# -*- encoding : utf-8 -*-
"""
@File       : product_model.py
@Time       :2021/1/22 14:32
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

from mall.db.models import Base

from sqlalchemy import Column, String, Float


class Product(Base):
    __tablename__ = 'product'

    product_id = Column(String(50), primary_key=True)
    product_name = Column(String(255))
    product_in_price = Column(Float)
    product_sell_price = Column(Float)
    product_discount_price = Column(Float)
    product_info = Column(String(1024))
    product_main_photo = Column(String(255))
    product_nums = Column(String(10))
    product_unit = Column(String(5))
    product_type = Column(String(10))


