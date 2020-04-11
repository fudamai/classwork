#! python3.8
# -*- coding:utf-8 -*-
# author:fudamai
# task.py

"""task，导入爬虫，爬取百度的数据
"""

import os
import sys
import json
from celery import Celery


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.spider import get_data_from_url


app=Celery('task', broker="amqp://", backend="redis://localhost")
app.config_from_object('config')  # 加载配置，config.py

@app.task
def worker(url):
    data = get_data_from_url(url)
    print(json.loads(data))
    return json.loads(data)  # 返回结果，保存到redis