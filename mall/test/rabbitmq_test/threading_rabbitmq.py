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


def send():
    p = rabbitmqProducer()

    with p.get_connection():
        producer = p.get_channel(que_name)
        msg = "Hello World!"
        producer.basic_publish(exchange='', routing_key=que_name, body=msg)


def recive():
    c = rabbitmqConsumer()

    conn = c.get_connection()
    consumer = c.get_channel(que_name)


thread1 = threading.Thread(target=send)
thread2 = threading.Thread(target=recive)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

