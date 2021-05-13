# -*- encoding : utf-8 -*-
"""
@File       : demo1.py
@Time       :2021/5/8 15:14
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : get请求自动封装参数
"""
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://api.github.com/events', params=payload)

# https://api.github.com/events?key1=value1&key2=value2
print(r.url)

