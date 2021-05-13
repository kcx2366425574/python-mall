# -*- encoding : utf-8 -*-
"""
@File       : demo2.py
@Time       :2021/5/8 15:44
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import requests

# from PIL import Image
# from io import BytesIO


r = requests.get('https://api.github.com/events')
# 响应内容
print(r.text)
# 二进制响应内容
print(r.content)
# json响应内容
print(r.json())


# 以请求返回的二进制数据创建一张图片
# i = Image.open(BytesIO(r.content))

