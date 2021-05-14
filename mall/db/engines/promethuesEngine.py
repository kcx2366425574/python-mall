# -*- encoding : utf-8 -*-
"""
@File       : promethuesEngine.py
@Time       :2021/4/13 8:52
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import json

import requests

from mall.common.common import Fail
from mall.common.load_config import CONF
from prometheus_client import Counter, Gauge


class PromethuesUtil:

    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def get_Instantaneous_data(cls, params=None, method="query"):
        url = "{}{}".format(CONF.promethues.url, method)

        res = requests.get(url, params=params)

        if res.status_code != 200:
            raise Fail("query promethues fail")

        return json.loads(res.content)

    @classmethod
    def get_promql(cls, metric_name, time_qujian=None, offset=None, **kwargs):
        if kwargs is not None:
            condition = ",".join(['{}="{}"'.format(key, value) if not value.startswith("~")
                                  else '{}=~"{}"'.format(key, value[1:]) for key, value in kwargs.items()])
        else:
            condition = ""
        temp = "{" + condition + "}"
        sql = "{}{}".format(metric_name, temp)
        if time_qujian is not None:
            sql = "{}[{}]".format(sql, time_qujian)
        if offset is not None:
            sql = "{} offset {}".format(sql, offset)
        return sql


class PrometheusSendData:

    @classmethod
    def send_counter(cls, metrics_name, help_info, value=None):

        c = Counter(metrics_name, help_info)
        if value is not None:
            c.inc(value)
        else:
            c.inc()

    @classmethod
    def send_gauge(cls, metrics_name, help_info, value, inc=None):
        g = Gauge(metrics_name, help_info)

        if inc is None:
            g.set(value)
        else:
            if inc:
                g.inc(value)
            else:
                g.dec(value)


