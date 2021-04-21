# -*- encoding : utf-8 -*-
"""
@File       : client.py
@Time       :2021/4/21 16:39
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

import socket

from mall.cmd.chat import HOST, PORT

socketclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketclient.connect((HOST, PORT))

while True:
    msg = input(">>>>")

    if msg != "exit":
        socketclient.sendall(msg.encode("utf-8"))

    data = socketclient.recv(1024)

