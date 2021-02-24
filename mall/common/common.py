# -*- encoding : utf-8 -*-
"""
@File       : common.py
@Time       :2021/1/26 19:24
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import json

from oslo_log import log as logging
import traceback

LOG = logging.getLogger(__name__)


def result_ok(data=""):
    return {"errCode": None, "errMessage": None, "exceptionMsg": None, "flag": False, "resData": data}


def result_fail(error_code, params):
    return {"errCode": error_code, "errMessage": None, "exceptionMsg": None, "flag": False, "resData": None}


def result_error():
    error_code = "INTERNAL_ERROR"
    return {"errCode": error_code, "errMessage": None, "exceptionMsg": None, "flag": False, "resData": None}


class Fail(Exception):

    def __init__(self, error_code, params=None):
        self.error_code = error_code
        self.params = params

    def __str__(self):
        return self.error_code


# -----------------带参数的装饰器------------------
def deco_catch_func_exception(func_desc="内部方法"):
    def catch_exception(origin_func):
        def wrapper(*args, **kwargs):
            func_name = "未知函数"
            try:
                func_name = origin_func.__name__
                u = origin_func(*args, **kwargs)
                return u
            except Fail as e:
                LOG.info(e)
                raise Fail("{}-{} 方法返回: {}".format(func_desc, func_name, e))
            except Exception as e:
                traceback.print_exc()
                LOG.error(e)
                raise Fail("{}-{} 方法异常: {}".format(func_desc, func_name, e))

        return wrapper

    return catch_exception


def deco_catch_view_exception(func_desc="外部接口"):
    def catch_exception(origin_func):
        def wrapper(*args, **kwargs):
            func_name = "未知函数"
            try:
                func_name = origin_func.__name__
                LOG.info(">>>执行功能--{}>>>".format(func_desc))
                u = origin_func(*args, **kwargs)
                return json.dumps(result_ok(u))
            except Fail as e:
                LOG.info(e)
                raise json.dumps(result_fail(e.error_code, e.params))
            except Exception as e:
                traceback.print_exc()
                LOG.error(e)
                raise Fail("{}-{} 方法异常: {}".format(func_desc, func_name, e))

        return wrapper

    return catch_exception
