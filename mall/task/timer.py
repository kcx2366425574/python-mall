# -*- encoding : utf-8 -*-
"""
@File       : timer.py
@Time       :2021/5/14 18:20
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.blocking import BlockingScheduler


APSCHEDULE_INTERVAL = "interval"

executors = {
    'default': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(3)
}

job_defaults = {
    'coalesce': True,
    'max_instances': 3
}

sche = BlockingScheduler(executors=executors, job_defaults=job_defaults)


def add_alert_jobs():
    pass


def add_normal_task():
    sche.add_job(add_alert_jobs, APSCHEDULE_INTERVAL, seconds=60, id="")


def init_tasks():
    add_alert_jobs()
    add_normal_task()
    sche.start()
