# -*- encoding : utf-8 -*-
"""
@File       : threading_rabbitmq.py
@Time       :2021/3/5 17:27
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

import threading
from mall.db.engines.rabbitmqEngine import rabbitmqProducer, rabbitmqConsumer


que_name = "kuangcx"


def send(msg):
    p = rabbitmqProducer()

    with p.get_connection():
        producer = p.get_channel(que_name)
        producer.basic_publish(exchange='', routing_key=que_name, body=msg)


def recive():
    c = rabbitmqConsumer()

    conn = c.get_connection()
    consumer = c.get_channel(que_name)


for i in range(5):
    threading.Thread(target=send, args=("这是消息{}".format(i), )).start()
thread2 = threading.Thread(target=recive)

thread2.start()

thread2.join()

