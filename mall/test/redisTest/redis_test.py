# -*- encoding : utf-8 -*-
"""
@File       : redis_test.py
@Time       :2021/3/4 19:56
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
from mall.common.load_config import load_config
from mall.db.engines.redisEngine import redisInstance

load_config()
client = redisInstance.get_client()
client.set("name", "kuangcx")
name = client.get("name")

print(name)