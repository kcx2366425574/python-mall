# -*- encoding : utf-8 -*-
"""
@File       : task_start.py
@Time       :2021/5/14 18:12
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""


from mall.common.load_config import load_config
from mall.task.timer import init_tasks


if __name__ == '__main__':

    load_config()

    init_tasks()
