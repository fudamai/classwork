#! python
# -*- coding:utf-8 -*-
# Author:fudamai
# ssh_cli.py

import os
import argparse
import configparser
import logging
import paramiko
from ssh_config import Config


"""用户名密码登录
密钥登录
命令行管理
-s 自定义连接主机
-u 上传文件
-d 下载文件
-c 进入交互控制台。默认不给定命令行参数时，进入此模式。
"""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
paramiko.util.log_to_file('fubai-ssh.log')
logging.basicConfig(filename='ssh_log.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class AcceptPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        "定义接收密钥的行为"
        return


class MiniSSH:
    def __init__(self, host, user, password):
        self.client = self.connect(host, user, password)
    
    def connect(self, host, user, password):
        "连接服务器"
        client = '' 
        try:  # 添加异常处理
            client = paramiko.SSHClient()  # 启动客户端
            client.set_missing_host_key_policy(AcceptPolicy())  # 警告处理
            print(type(host))
            client.connect(host, username=user, password=password)
            # client.connect(host, username=user)  # 使用密钥连接
            print(client)
            logging.info(f'用户{user}SSH登录{host}成功，')
        except Exception as e:
            print(e)
            logging.debug(f'SSH登录失败，错误：{e}')
            return False
        return client

    def close(self):
        "定义关闭client的方法"
        self.client.close()
        logging.debug('client已关闭')

    def send_cmd(self, cmd):
        """发送命令，取得返回值"""
        try:
            stdin, stdout, stderr = self.client.exec_command(cmd)
            # print(stdin, stdout, stderr)
            logging.debug('发送命令到远端执行成功，并返回结果')
            return stdout
        except paramiko.SSHException as e:  # SSH异常判断
            print(e)
            logging.debug('发送命令到远端出现异常')

    def upload_file(self, local_file_path, remote_file_path):
        """把本地文件上传到服务器，put"""
        ret = {"status":0, "msg":"upload ok"}
        try:
            if self.client:
                ftp_client = self.client.open_sftp()
                ftp_client.put(local_file_path, remote_file_path)  # 从本地路径上传至远程路径
                ftp_client.close()
                logging.info('上传文件到远端成功')
            else:
                logging.warning('上传文件时，client连接失败')
                ret['status'] = 1
                ret['msg'] = 'client false'
        except Exception as e:
            print(e)
            logging.debug(e)
            ret['status'] = 2
            ret['msg'] = e
        return ret

    def download_file(self, remote_file_path, local_file_path):
        """从服务器下载文件，get"""
        ret = {"status":5, "msg":"download ok"}
        try:
            if self.client:
                ftp_client = self.client.open_sftp()
                ftp_client.get(remote_file_path, local_file_path)  # 从远端路径下载到本地
                ftp_client.close()
                logging.info('从远端下载文件成功')
            else:
                logging.warning('下载文件时，client连接失败')
                ret['status'] = 3
                ret['msg'] = 'client false'
        except Exception as e:
            print(e)
            logging.debug(e)
            ret['status'] = 4
            ret['msg'] = e
        return ret


def parser_group():
    """定义命令行组
    """
    parser = argparse.ArgumentParser("fubai SSH功能列表")
    # group1
    group1 = parser.add_argument_group('group1', '第一组，基本命令')
    # verbose
    group1.add_argument('-s', '--ssh', dest="ssh", nargs=2, help="ssh连接 -s [username] [ip]")
    group1.add_argument('-c', dest="cmd", action="store_true", help="进入交互控制台")

    group2 = parser.add_argument_group('group2', '第二组，上传与下载文件')
    # upload
    group2.add_argument('-u', '--upload', dest="upload", nargs=2, help="上传文件，-u local-file remote-file")
    # download
    group2.add_argument('-d', '--download', dest="download", nargs=2, help="上传文件，-d remote-file local-file") 

    return parser 


def main():
    """执行main函数时，未指定情况下，使用默认配置用户登录
    """
    admin = Config('192.168.235.132')
    host, username, password = admin.load_config()
    client = MiniSSH(host, username, password)
    logging.info('连接默认的主机')
    parser = parser_group()
    args = parser.parse_args()

    if args:
        parser.print_help()
    if args.ssh:
        # 自定义登录
        username = args.ssh[0]
        host = args.ssh[1]
        password = input(f'{username}@{host}的密码：')
        client = MiniSSH(host, username, password)
        Config(host).add_section(username, password)  # 自动添加用户配置
        logging.info('使用SSH命令指定连接的主机')
    elif args.upload:
        # 使用默认用户登录
        local_file_path = input('请输入本地文件路径：')
        remote_file_path = input('请输入远端文件路径：')
        stdout = client.upload_file(local_file_path,  remote_file_path)
        print(stdout)
    elif args.download:
        # 使用默认用户登录
        local_file_path = args.download[1]
        remote_file_path = args.download[0]
        stdout = client.download_file(remote_file_path, local_file_path)
        print(stdout)

    if not client:
        return
    else:
        while True:
            print('输入命令[q]-退出')
            cmd = input('>>')
            if cmd == 'q':
                client.close()
                break
            elif cmd == '-u':
                print('上传文件到远端。')
                local_file_path = input('请输入本地文件路径：')
                remote_file_path = input('请输入远端文件路径：')
                stdout = client.upload_file(local_file_path,  remote_file_path)
                print(stdout)
            elif cmd == '-d':
                # client = MiniSSH()
                print('从远端下载文件。')
                local_file_path = input('请输入本地文件路径：')
                remote_file_path = input('请输入远端文件路径：')
                stdout = client.download_file(remote_file_path, local_file_path)
                print(stdout)
            else:
                stdout = client.send_cmd(cmd)
                print(stdout.read().decode())

# 为完成项：添加读取配置,自动登录

if __name__ == "__main__":
    main()