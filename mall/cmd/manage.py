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


def main():
    load_config()
    table_sync()


def table_sync():
    from mall.db.models.product.product_model import Product
    tables = [
        Base.metadata.tables["product"]
    ]
    Base.metadata.create_all(get_engine(), tables=tables, checkfirst=True)


if __name__ == '__main__':
    main()
