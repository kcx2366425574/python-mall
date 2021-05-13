# -*- encoding : utf-8 -*-
"""
@File       : common_decoration.py
@Time       :2021/5/10 15:03
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

import time
from functools import wraps
from inspect import signature


# 保留函数的元信息
def timethis_with_data(func_desc="外部接口"):
    '''
    Decorator that reports the execution time.
    '''
    def catch_exception(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("执行函数:-------->>>", func_desc)
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(func.__name__, end-start)
            return result
        return wrapper
    return catch_exception


# 不保留函数的元信息
def timethis(func_desc="外部接口"):
    '''
    Decorator that reports the execution time.
    '''
    def catch_exception(origin_func):
        def wrapper(*args, **kwargs):
            print("执行函数:-------->>>", func_desc)
            start = time.time()
            result = origin_func(*args, **kwargs)
            end = time.time()
            print(origin_func.__name__, end-start)
            return result
        return wrapper
    return catch_exception


# 对参数的类型进行校验
def type_assert(*ty_args, **ty_kwargs):
    def catch_exception(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                        )
            return func(*args, **kwargs)
        return wrapper
    return catch_exception
