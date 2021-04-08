# -*- encoding : utf-8 -*-
"""
@File       : tqdm_demo4.py
@Time       :2021/4/8 16:57
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : 手动控制进度，加一个tqdm上下文
"""
from time import sleep

from tqdm import tqdm


"""
pbar 是 tpdm 的“进度”，每一次对 pbar 进行 update 10 都相当于进度加10。
Total 的值即是总进度，这里 total 的值是100，那么pbar加到100的时候进度也就结束了
"""
with tqdm(total=100) as pbar:
    for i in range(10):
        sleep(0.1)
        pbar.update(10)
