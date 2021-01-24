# -*- encoding : utf-8 -*-
"""
@File       : constant.py
@Time       :2021/1/22 15:55
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : constant in the project
"""
import os

from oslo_config import cfg

CONF = cfg.CONF

# os.path.dirname(path) 获取path路径的上级目录
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

RESOURCE_PATH = os.path.join(BASE_DIR, 'resource')
CONF_FILE_DIR = os.path.join(RESOURCE_PATH, 'conf')
CONF_FILE_PATH = os.path.join(CONF_FILE_DIR, 'mall.conf')

