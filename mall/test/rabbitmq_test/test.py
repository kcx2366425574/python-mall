# -*- encoding : utf-8 -*-
"""
@File       : test.py
@Time       :2021/3/5 15:44
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
from mall.common.load_config import load_config
from mall.db.engines.rabbitmqEngine import rabbitmqProducer, rabbitmqConsumer

load_config()
p = rabbitmqProducer()

c = rabbitmqConsumer()
with p.get_connection() as f:
    producer = p.get_channel("kuangcx")
    conn = c.get_connection()

    producer.basic_publish(exchange='', routing_key='kuangcx', body='Hello World!')

    consumer = c.get_channel("kuangcx")
