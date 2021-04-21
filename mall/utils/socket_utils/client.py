# -*- encoding : utf-8 -*-
"""
@File       : client.py
@Time       :2021/4/12 14:50
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口号

s.connect((host, port))
s.recv(1024)
s.close()