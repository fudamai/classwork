#! python
# -*- coding:utf-8 -*-
# Author:fudamai
# http_2.py


import os
import socket
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print(BASE_DIR)


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
        if path == '/':
            with open(os.path.join(BASE_DIR, 'pic', 'home.html'), mode='rt', encoding='utf-8') as h:
                HTML = h.read()
            response = HTML.encode()  # 编码为字节流bytes'gbk'
            conn.sendall(response)  # 在这里处理数据
        elif path == '/json':
            response = """HTTP/1.1 200 OK

            <a href='http://localhost:8888'>link</a>
            
            {"k":"v", "name":"fubai", "msg":"传送中文"}

            """.encode('gbk')  # 编码为字节流bytes,'gbk'格式为中文
            conn.sendall(response)  # 在这里处理数据
        elif path == '/pic/1.jpg':
            response = f"""HTTP/1.1 200 OK

            <a href='http://localhost:8888'>link</a>

            <h1>付立爽的第一个图片</h1>

            <img class="main_img img-hover" data-imgurl="https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1326800567,3725737690&amp;fm=26&amp;gp=0.jpg" src="https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1326800567,3725737690&amp;fm=26&amp;gp=0.jpg" style="background-color: rgb(189, 171, 169); width: 234px; height: 165.585px;">

            """.encode('gbk')            
            conn.sendall(response)  
        
    else:
        print(data)

    conn.close()

# 关闭socket
# sock.close()