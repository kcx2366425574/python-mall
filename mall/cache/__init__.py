# -*- encoding : utf-8 -*-
"""
@File       : __init__.py.py
@Time       :2021/1/26 18:53
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

from oslo_cache import core as cache
from oslo_config import cfg

from mall.common.load_config import CONF

caching = cfg.BoolOpt('caching', default=True)
cache_time = cfg.IntOpt('cache_time', default=3600)
CONF.register_opts([caching, cache_time], "feature-name")

cache.configure(CONF)
example_cache_region = cache.create_region()
MEMOIZE = cache.get_memoization_decorator(
    CONF, example_cache_region, "feature-name")

# Load config file here

cache.configure_cache_region(CONF, example_cache_region)
