# -*- encoding : utf-8 -*-
"""
@File       : consumer.py
@Time       :2021/3/11 15:36
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
from mall.db.engines.rabbitmqEngine import rabbitmqConsumer

que_name = "kuangcx"


def get_index(ch, method, properties, body):
    string = str(body, encoding="utf-8")
    msg = dict(eval(string))
    print(msg.get("index"))


c = rabbitmqConsumer()

conn = c.get_connection()
consumer = c.get_channel(que_name, on_message_callback=get_index)
