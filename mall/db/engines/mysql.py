# -*- encoding : utf-8 -*-
"""
@File       : mysql.py
@Time       :2021/1/22 14:50
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import threading

from oslo_db.sqlalchemy import session as db_session
from oslo_db import options
from mall.common.load_config import CONF

options.set_defaults(CONF, connection=r"sqlite:///test.db")
_LOCK = threading.Lock()
_FACADE = None


def _create_facade_lazily():
    global _LOCK
    with _LOCK:
        global _FACADE
        if _FACADE is None:
            _FACADE = db_session.EngineFacade(
                CONF.database.connection, **dict(CONF.database)
            )

        return _FACADE


def get_engine():
    facade = _create_facade_lazily()
    return facade.get_engine()


def get_session(**kwargs):
    facade = _create_facade_lazily()
    return facade.get_session(**kwargs)
