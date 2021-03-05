# -*- encoding : utf-8 -*-
"""
@File       : producer.py
@Time       :2021/3/5 14:03
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import pika

# auth = pika.PlainCredentials('root', 'root')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', port=5672))
channel = connection.channel()

channel.queue_declare(queue='TEST01')

channel.basic_publish(exchange='', routing_key='TEST01', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
