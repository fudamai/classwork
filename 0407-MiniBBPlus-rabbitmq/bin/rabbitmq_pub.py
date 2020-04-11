#! python3.8
# -*- coding:utf-8 -*-
# author:fudamai
# msg_pub.py
# 发送消息
# 消息的持久化，避免突发情况（如：断电）导致信息丢失
# 添加消息送达回执
# 写成类
# 实现发布、订阅

"""
再admin.py中调用此模块。在操作完成时，将操作内容发布
"""

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.basemq import FubaiMQ

class PubMQ(FubaiMQ):
    def __init__(self):
        super().__init__()


mq_client = PubMQ()

def fanout_pub(msg, exchange_name, mq_client=mq_client):
    mq_client.mk_exchange(exchange=exchange_name, exchange_type="fanout")
    mq_client.publish(msg=msg, routing_key="", exchange=exchange_name)
    print(f'发送消息{msg}')

def main():
    msg = " ".join(sys.argv[1:]) or "send a new message"
    mq_pub = PubMQ()
    mq_pub.mk_exchange(exchange="news", exchange_type="fanout")
    # queue_name = mq_pub.make_random_queue()
    # mq_pub.bind_queue(queue_name, "news")
    mq_pub.publish(msg=msg, routing_key="", exchange="news")  # 使用fanout模式实现发布订阅，只需再接收端绑定队列名即可。发送端无需绑定

    print(f"发送消息：{msg}") 


if __name__ == "__main__":
    main()