# -*- encoding : utf-8 -*-
"""
@File       : manage.py
@Time       :2021/1/22 15:42
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import os
import pathlib
import sqlacodegen

from mall.db.models import Base
from mall.db.engines.mysql import get_engine
from mall.common.load_config import load_config, CONF
from mall.utils import mysql_utils
from mall.utils.mysql_utils import SQLgo


def main():
    # load_config()
    generate_data("localhost", "root", "root", 3306, "mall")


def table_sync():
    from mall.db.models.product.product_model import Product
    tables = [
        Base.metadata.tables["product"]
    ]
    Base.metadata.create_all(get_engine(), tables=tables, checkfirst=True)


def generate_data(ip, user, password, port, db):

    with SQLgo(ip=ip, user=user, password=password, port=port, db=db) as session:
        tables = session.get_tables()


if __name__ == '__main__':
    main()
