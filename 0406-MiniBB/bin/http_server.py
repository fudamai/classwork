#! python
# -*- coding:utf-8 -*-
# Author:fudamai
# http_server.py


import os
import socket
import sys
import json
import re
import redis

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print(BASE_DIR)

from bin.admin import Admin

article_extract = Admin()
pattern = re.compile('/article/')  # 建立正则，用于分割url，以提取id
client = redis.Redis(host='localhost', port=6379, db=1)

HOST = ''  # localhost:本机，ip值， 空：任意主机都可以访问
PORT = 8888
ADDR = (HOST, PORT)
BUFSIZE = 1024

# 新建socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TCP相关参数.TCP 发送字节流

# 绑定地址
sock.bind(ADDR)

# 监听连接的个数
sock.listen(1)

print('启动http服务')

# 循环发送和接收数据
while True:
    print('等待连接')
    conn, addr = sock.accept()
    print('成功连接：', addr)

    # 循环接收    
    data = conn.recv(BUFSIZE)
    print('收到数据：', data)  # 处理中文数据的显示问题
     
    if data:
        req_path = data.decode('utf-8').splitlines()[0]
        print('收到数据第一行：', req_path)  # 处理中文数据的显示问题
        method, path, http = req_path.split()
        print(f'切换URL地址到{path}')
        # pattern.split(path)[1] == None
        if path == '/':
            with open(os.path.join(BASE_DIR, 'db', 'home.html'), mode='rt', encoding='utf-8') as h:
                HTML = h.read()
            response = HTML.encode()  # 编码为字节流bytes'gbk'
            conn.sendall(response)  # 在这里处理数据
        elif path == '/article/all':
            json = article_extract.query_article_to_json(id=None, mode=2)  # 注意，相应必须时HTML格式
            
            response = f"""HTTP/1.1 200 OK

{json}

            """.encode('gbk')
            print(response)
            conn.sendall(response)  # 在这里处理数据
        elif path == '/article/id':
            response = f"""HTTP/1.1 200 OK

<a href='http://localhost:8888'>home</a>

<h1>请手动输入url,指定文章的id</h1>

            """.encode('gbk')
            conn.sendall(response)
        elif len(path) > 9:
            # id= pattern.split(path) # 匹配出文章id
            try:
                id = pattern.split(path)[1]
                # id = path.split('/')[2]
                print(id)
                # 2137531153
                json = article_extract.query_article_to_json(int(id), mode=1)
                response = f"""HTTP/1.1 200 OK

{json}

                """.encode('gbk')

                conn.sendall(response)
                client.incr(f'article:{id}')
            except Exception as e:
                print(e, '404')
        else:  # URL 不正确，返回404
            response = f"""HTTP/1.1 200 OK

<h1>404</h1>
            
            """.encode('gbk')
            conn.sendall(response)
        
    else:
        print(data)

    conn.close()

# 关闭socket
# sock.close()