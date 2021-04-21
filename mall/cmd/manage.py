# -*- encoding : utf-8 -*-
"""
@File       : manage.py
@Time       :2021/1/22 15:42
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

from mall.db.models import Base
from mall.db.engines.mysql import get_engine
from mall.common.load_config import load_config
from mall.utils import mysql_utils
from mall.utils.mysql_utils import SQLgo


def main():
    # load_config()
    generate_data()


def table_sync():
    from mall.db.models.product.product_model import Product
    tables = [
        Base.metadata.tables["product"]
    ]
    Base.metadata.create_all(get_engine(), tables=tables, checkfirst=True)


def generate_data():
    with SQLgo(ip="10.48.66.58", user="root", password="123456a?", port=3306) as engine:
        databases = engine.get_database()
    # databases = []

    for db in databases:
        with SQLgo(ip="10.48.66.58", user="root", password="123456a?", port=3306, db=db) as session:
            session.get_tables()


if __name__ == '__main__':
    main()
