#! python3.8
# -*- coding:utf-8 -*-
# author:fudamai
# basemq.py
# mq基类


import os
import sys
import time
import pika

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.setting import CONFIG


class FubaiMQ:
    def __init__(self):
        self.connection = self.mk_connect()
        self.channel = self.connection.channel()

    def mk_connect(self):
        """连接服务"""
        ## 添加配置文件，自动分析用户、主机
        # CONFIG = {
        #     "username": "fubai",
        #     "password": "12341234",
        #     "host": "192.168.235.131",
        #     "port": ""
        # }
        creds = pika.PlainCredentials(CONFIG["username"],CONFIG["password"])
        params = pika.ConnectionParameters(CONFIG["host"], credentials=creds)
        connection = pika.BlockingConnection(params)
        return connection
        
    def mk_exchange(self, exchange='news', exchange_type='fanout'):
        """创建交换，用于指定类型
        """
        self.channel.exchange_declare(exchange=exchange,  exchange_type=exchange_type)

    def make_random_queue(self):
        """自动分配队列名
        """
        q = self.channel.queue_declare("",   exclusive=True)
        return q.method.queue  # 输出queue的名字

    def bind_queue(self, queue, exchange, routing_key=None):
        """绑定交换与队列
        """
        self.channel.queue_bind(queue, exchange, routing_key)

    def mk_queue(self, queue_name):
        """创建队列
        """
        self.channel.queue_declare(queue=queue_name, durable=True)
        # durable持久化参数
        return self.channel

    def publish(self, msg, routing_key, exchange=""):
        """发送消息
        """        
        self.channel.basic_publish(exchange=exchange, 
                    routing_key=routing_key, 
                    body=msg, 
                    properties=pika.BasicProperties(delivery_mode=2  #持久化消息
        ))
        # print(f"发送消息：{msg}")

    def callback(self, channel, method, priperties, body):
        """默认定义的callback函数
        """
        print(f"收到消息:{body.decode()}")
        # time.sleep(body.decode().count("-"))
        print('ok')
        channel.basic_ack(delivery_tag=method.delivery_tag)  # 定义回执
        return self.callback

    def consume(self, queue_name):
        """
        接收消息
        """
        self.channel.basic_qos(prefetch_count=1)  # 定义消息预取规则
        self.channel.basic_consume(queue_name, self.callback)
        self.channel.start_consuming()

    def close_connect(self):
        self.connection.close()


def main():
    msg = sys.argv[1:] or "send a new message"
    MQ = FubaiMQ()
    MQ.publish(msg=msg, routing_key="q1")

    print(f"发送消息：{msg}") 


if __name__ == "__main__":
    main()