# -*- encoding : utf-8 -*-
"""
@File       : migration.py
@Time       :2021/1/24 10:14
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import os

from oslo_db.sqlalchemy.migration import db_sync
from oslo_db.sqlalchemy.migration import db_version

from mall.db.engines.mysql import get_engine

INIT_VERSION = 000

MIGRATE_REPO_PATH = os.path.join(os.path.join(
    os.path.dirname(__file__)), 'migrate_repo',
)


def get_db_version(init_version=INIT_VERSION, engine=None):
    if engine is None:
        engine = get_engine()

    version = db_version(engine, MIGRATE_REPO_PATH, init_version)

    return version


def exec_db_sync(version=None, init_version=INIT_VERSION, engine=None):
    if engine is None:
        engine = get_engine()

    db_sync(engine=engine, abs_path=MIGRATE_REPO_PATH, version=version, init_version=init_version)


if __name__ == '__main__':
    print(get_db_version())

