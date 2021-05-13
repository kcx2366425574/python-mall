# -*- encoding : utf-8 -*-
"""
@File       : prometheus_task.py
@Time       :2021/4/23 10:16
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

from prometheus_client import CollectorRegistry, Gauge, pushadd_to_gateway

def push2gateway(datas):

    registry = CollectorRegistry()

    g = Gauge('node_process_status_info','process monitor',['group','process_name','status','days','icon'],registry=registry)

    for group,process,status,runtime,icon in datas:

        print(group,process,status,runtime,icon)

        g.labels(group,process,status,str(runtime),icon).set(icon)

    pushadd_to_gateway('10.10.148.34:9091', job='pushgateway' ,registry=registry,timeout=200)