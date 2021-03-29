# -*- encoding : utf-8 -*-
"""
@File       : __init__.py.py
@Time       :2021/3/29 16:01
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

# 建立一个sshclient对象
import paramiko

ssh = paramiko.SSHClient()
# 允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 调用connect方法连接服务器
ssh.connect(hostname='10.48.66.220', port=22, username='kuangcx', password='123456a?')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('docker ps')
# 结果放到stdout中，如果有错误将放到stderr中
print(stdout.read().decode())
# 关闭连接
ssh.close()
