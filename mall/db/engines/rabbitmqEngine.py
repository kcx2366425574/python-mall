# -*- encoding : utf-8 -*-
"""
@File       : rabbitmqEngine.py
@Time       :2021/3/5 11:32
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import pika

from mall.common.load_config import CONF


class rabbitBase:
    _connection = None

    def __init__(self):
        self._connection = self.get_connection()

    @classmethod
    def get_connection(cls):
        def __enter__():
            return

        def __exit__():
            cls._connection.close()

        if cls._connection is None:
            pika.PlainCredentials(CONF.rabbitmq.user, CONF.rabbitmq.password)
            return pika.BlockingConnection(
                pika.ConnectionParameters(host=CONF.rabbitmq.host, port=CONF.rabbitmq.port))
        return cls._connection


class rabbitmqProducer(rabbitBase):

    @classmethod
    def get_channel(cls, que_name):
        channel = cls.get_connection().channel()
        channel.queue_declare(queue=que_name)
        return channel


class rabbitmqConsumer(rabbitBase):

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    @classmethod
    def get_channel(cls, que_name, on_message_callback=callback):
        channel = cls.get_connection().channel()
        channel.queue_declare(queue=que_name)

        channel.basic_consume(on_message_callback=on_message_callback,
                              queue=que_name,
                              auto_ack=CONF.rabbitmq.auto_ack)
        channel.start_consuming()
        return channel
