# -*- encoding : utf-8 -*-
"""
@File       : file_transport.py
@Time       :2021/3/31 17:32
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : 实现文件的远程传输
"""
import os
import paramiko


class SCPTransmitter:

    def __init__(self):

        # <host name>为远程计算机主机名（云服务器公网IP）
        # <port>为端口号，云服务器默认为22，使用其他端口需要到安全组配置放开端口
        # <user name>为登录用户名，阿里云默认为root
        # <public key path>为登录云服务器的密钥文件路径
        self.hostname = 'kuangcx'
        self.port = 22
        self.username = 'kuangcx00'

        self.public_key = paramiko.RSAKey.from_private_key_file('<public key path>')
        self.scp = paramiko.Transport(self.hostname, self.port)
        self.scp.connect(username=self.username, pkey=self.public_key)
        self.sftp = paramiko.SFTPClient.from_transport(self.scp)

    '''
        Description:
            download remote files from remote server
        Args:
            remote_path:
                remote dirctory of files wanna download
            local_path:
                local path to save files
        Returns:
            None
    '''

    def download(self, remote_path, local_path):
        try:
            remote_files = self.sftp.listdir(remote_path)
            for file in remote_files:
                local_file = local_path + file
                print(local_file)
                remote_file = remote_path + file
                print(remote_file)
                self.sftp.get(remote_file, local_file)
            print("Successfully")
        except IOError:
            return "remote_path or local_path is not exist"

    '''
        Description:
            upload local files to remote server
        Args:
            remote_path:
                remote dirctory to save files
            local_path:
                local directory of files wanna upload 
    '''

    def upload(self, remote_path, local_path):
        try:
            local_files = os.listdir(local_path)
            print(local_files)
            for file in local_files:
                local_file = local_path + file
                print(local_file)
                remote_file = remote_path + file
                print(remote_file)
                self.sftp.put(local_file, remote_file)
            print("Successfully")
        except IOError:
            return "remote_path or local_path is not exist"


if __name__ == "__main__":
    remote_path = '/home/remote/'
    local_path = './res/remote/'
    transmitter = SCPTransmitter()
    transmitter.upload(remote_path, local_path)
