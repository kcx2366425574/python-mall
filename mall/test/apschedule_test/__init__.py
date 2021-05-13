# -*- encoding : utf-8 -*-
"""
@File       : __init__.py.py
@Time       :2021/5/11 10:35
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import time
from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

run_time = None


def count():
    print(1)
    time.sleep(5)
    print(2)
    time.sleep(5)
    print(3)
    time.sleep(5)
    print(4)
    time.sleep(5)
    print(5)
    time.sleep(5)
    print(6)
    time.sleep(5)


if __name__ == '__main__':
    sche = BackgroundScheduler()
    sche.add_job(count, "interval", seconds=5, id="count")
    sche.start()

    time.sleep(6)
    print("休眠截止")
    sche.pause_job("count")
    time.sleep(60)
    # while True:
    #
    #     now = datetime.now()
    #     if run_time is not None and now - timedelta(seconds=9) < run_time:
    #         job = sche.get_job("count")
    #         job.pause()
    #         print("休眠开始")
    #         time.sleep(30)
    #         print("休眠截止")
    #         job.resume()
