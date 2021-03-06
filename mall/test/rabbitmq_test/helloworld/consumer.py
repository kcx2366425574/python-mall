# -*- encoding : utf-8 -*-
"""
@File       : consumer.py
@Time       :2021/3/5 14:04
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import pika

# auth = pika.PlainCredentials('root', 'root')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', port=5672))
channel = connection.channel()

channel.queue_declare(queue='TEST01')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(on_message_callback=callback,
                      queue='TEST01',
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

