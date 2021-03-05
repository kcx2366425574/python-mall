# -*- encoding : utf-8 -*-
"""
@File       : redisEngine.py
@Time       :2021/3/4 19:04
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import redis

from mall.common.load_config import CONF


class redisInstance:

    _instance = None

    def __init__(self):
        self.host = CONF.redis.host
        self.port = CONF.redis.port
        self.password = CONF.redis.password
        self.timeout = CONF.redis.timeout
        self.db = CONF.redis.database

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def get_client(cls):

        instance = cls.get_instance()
        client = redis.StrictRedis(
            host=instance.host,
            port=instance.port,
            password=instance.password,
            db=instance.db,
            socket_timeout=instance.timeout
        )

        return client
