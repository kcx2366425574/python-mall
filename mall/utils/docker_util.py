# -*- encoding : utf-8 -*-
"""
@File       : docker_util.py
@Time       :2021/4/9 10:48
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import docker

client = docker.from_env()

print(client.version())