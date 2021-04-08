# -*- encoding : utf-8 -*-
"""
@File       : tqdm_demo3.py
@Time       :2021/4/8 16:56
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : 控制进度条显示当前步骤的名称
"""
from time import sleep

from tqdm import tqdm

pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    sleep(0.25)
    pbar.set_description("Processing %s" % char)