# -*- encoding : utf-8 -*-
"""
@File       : client.py
@Time       :2021/4/8 18:47
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

from mall.utils.gpc import rpcclient

c = rpcclient.RPCClient()
c.connect('127.0.0.1', 5000)
res = c.add(1, 2, c=3)
print(f'res: [{res}]')