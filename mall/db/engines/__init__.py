# -*- encoding : utf-8 -*-
"""
@File       : __init__.py.py
@Time       :2021/1/22 14:29
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
from oslo_config import cfg

from mall.common.load_config import CONF

# 注册配置文件中的section
redis_group = cfg.OptGroup(name="redis", title="redis")

redis_opts = [
    cfg.StrOpt("host", default="10.48.66.220", help="the redis host"),
    cfg.IntOpt("port", default=6379, help="the redis port"),
    cfg.StrOpt("password", default="123456a?", help="the redis password"),
    cfg.IntOpt("timeout", default=6000, help="the redis socket timeout"),
    cfg.IntOpt("database", default=0, help="the redis database nnum")
]

CONF.register_group(redis_group)

CONF.register_opts(redis_opts, redis_group)

# 注册配置文件中的rabbitmq section
rabbitmq_group = cfg.OptGroup(name="rabbitmq", title="rabbitmq")

rabbitmq_opts = [
    cfg.StrOpt("host", default="127.0.0.1", help="the rabbitmq host"),
    cfg.IntOpt("port", default=5672, help="the rabbitmq port"),
    cfg.StrOpt("user", default="root", help="the rabbitmq user"),
    cfg.StrOpt("password", default="root", help="the rabbitmq password"),
    cfg.BoolOpt("auto_ack", default=True, help="the rabbitmq auto ack flag")
]

CONF.register_group(rabbitmq_group)

CONF.register_opts(rabbitmq_opts, rabbitmq_group)
