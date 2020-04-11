#! python3.8
# -*- coding:utf-8 -*-
# author:fudamai
# redis_sub.py
# redis sub/pub demo
# 接收端


"""作为客户端，当服务端对服务器进行操作时。接收操作内容
使用redis实现订阅

"""

import redis


client = redis.StrictRedis()

channels = ["show","add", "delete"]

# 得到pubsub对象
# 订阅对象
# listen监听频道

def subscribe():
    s1 = client.pubsub()
    s1.subscribe("show")
    
    # input()选择监听哪个频道
    s2 = client.pubsub()
    s2.subscribe("add")

    s3 = client.pubsub()
    s3.subscribe("delete")

    show_msg(s1, "show")
    show_msg(s2, "add")
    show_msg(s3, "delete")

    print('接收到订阅信息')

def show_msg(sub_obj, sub_name):
    for msg in sub_obj.listen():
        if msg["type"] == 'message':
            print(f"{sub_name} get {msg['data'].decode()} from {msg['channel']}")



def main():
    subscribe()

if __name__ == "__main__":
    main()