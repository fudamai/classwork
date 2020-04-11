#! python3.8
# -*- coding:utf-8 -*-
# author:fudamai
# msg_worker.py
# 接受消息及其它工作
# 添加中文转码
# 消息的持久化
# 实现订阅功能

import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.basemq import FubaiMQ

channel_list = ['show', 'add', 'delete']

class WorkerMQ(FubaiMQ):
    def __init__(self):
        super().__init__()

def fanout_sub(channel):
    mq_consum = WorkerMQ()
    mq_consum.mk_exchange(exchange=channel, exchange_type="fanout")
    queue_name = mq_consum.make_random_queue()
    mq_consum.bind_queue(queue_name, channel)  # 使用fanout模式实现发布订阅，只需再接收端绑定队列名即可。发送端无需绑定
    mq_consum.consume(queue_name)    
    mq_consum.close_connect()

def main():
    """由于rabbitmq持续监听指定exchange，
    这里使用多线程让rabbitmq-server监听多个exchange
    """

    with ThreadPoolExecutor(3, thread_name_prefix='fuabi') as executor:
        futures = [executor.submit(fanout_sub, channel) for channel in channel_list]
        for future in as_completed(futures):
            try:
                print(future.result())
            except Exception as e:
                print(e)


if __name__ == "__main__":
    main()