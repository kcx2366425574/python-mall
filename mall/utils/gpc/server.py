# -*- encoding : utf-8 -*-
"""
@File       : server.py
@Time       :2021/4/8 18:52
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

from mall.utils.gpc import rpcserver


def add(a, b, c=10):
    sum = a + b + c
    return sum


s = rpcserver.RPCServer()
# 注册方法
s.register_function(add)
# 传入要监听的端口
s.loop(5000)
