# -*- encoding : utf-8 -*-
"""
@File       : producer.py
@Time       :2021/3/11 15:36
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import json
import threading

from mall.db.engines.rabbitmqEngine import rabbitmqProducer

que_name = "kuangcx"


def produce_info(i):
    pro = rabbitmqProducer()
    with pro.get_connection():
        print(i)
        producer = pro.get_channel(que_name)
        body = {
            "index": i
        }
        producer.basic_publish(exchange='', routing_key=que_name, body=json.dumps(body))


for i in range(20):
    threading.Thread(target=produce_info, args=(i,)).start()
