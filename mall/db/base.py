# -*- encoding : utf-8 -*-
"""
@File       : base.py
@Time       :2021/1/26 20:36
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
from oslo_db.sqlalchemy import models


class DBbase(models.ModelBase):

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
