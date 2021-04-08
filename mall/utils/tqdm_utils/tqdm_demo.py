# -*- encoding : utf-8 -*-
"""
@File       : tqdm_demo.py
@Time       :2021/4/8 16:51
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

from tqdm import tqdm
from time import sleep

text = ""
for char in tqdm(["a", "b", "c", "d"]):
    sleep(0.25)
    text = text + char
