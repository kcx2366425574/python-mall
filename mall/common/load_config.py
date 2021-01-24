# -*- encoding : utf-8 -*-
"""
@File       : load_config.py
@Time       :2021/1/22 15:36
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : 加载配置文件
"""

from mall.common.constant import CONF_FILE_PATH
from oslo_config import cfg

CONF = cfg.CONF


def load_config():
    CONF(['--config-file', CONF_FILE_PATH], project="mall")
