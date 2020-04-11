#! python3.8
# -*- coding:utf-8 -*-
# author:fudamai
# config.py

"""
添加时间配置
让task按时间执行
"""

from celery.schedules import crontab

CELERY_TIMEZONE = 'Asia/Shanghai'  # 设置时区
CELERYBEAT_SCHEDULE = {
    'once-everyday':{
        'task':'task.worker', # 需执行的函数
        # 'schedule':crontab(minute=0, hour=12),  # 每天中午12点执行1次
        'schedule':crontab(minute='*/1'),  # 定时更改为每分钟一次，用于测试
        'args':('https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1',)
    }
}