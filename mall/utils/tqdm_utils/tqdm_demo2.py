# -*- encoding : utf-8 -*-
"""
@File       : tqdm_demo2.py
@Time       :2021/4/8 16:55
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
from time import sleep

from tqdm import trange

for i in trange(100):
    sleep(0.01)