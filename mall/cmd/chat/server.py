# -*- encoding : utf-8 -*-
"""
@File       : server.py
@Time       :2021/4/21 16:40
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

import socket
from mall.cmd.chat import HOST, PORT

socketserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketserver.bind((HOST, PORT))

socketserver.listen(10)
username = dict()

while True:
    conn, addr = socketserver.accept()

    data = conn.recv(1024).decode("utf-8")

    print("{}: --->{}".format(addr, data))


