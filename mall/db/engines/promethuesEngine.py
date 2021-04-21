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

        if params:
            params_in_url = "&".join(["{}={}".format(key, value) for key, value in params.items()])
            request_url = "{}?{}".format(url, params_in_url)
        else:
            request_url = url

        res = requests.get(request_url)

        if res.status_code != 200:
            raise Fail("query promethues fail")

        return json.loads(res.content)
