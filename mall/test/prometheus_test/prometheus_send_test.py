# -*- encoding : utf-8 -*-
"""
@File       : prometheus_send_test.py
@Time       :2021/5/11 9:28
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

# Create a metric to track time spent and requests made.
import random
import time

from prometheus_client import start_http_server, Summary

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())
