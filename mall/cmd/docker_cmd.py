# -*- encoding : utf-8 -*-
"""
@File       : docker_cmd.py
@Time       :2021/3/5 8:52
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

import docker

client = docker.Client(base_url='tcp://10.48.66.134:9527', version='20.10.1', timeout=5)
print(client.images())