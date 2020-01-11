#! python
# -*- coding:utf-8 -*-
# Author:fudamai
# log_fun.py

"""
日志配置模块
"""
import logging
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 取给定路径上一级的路径



log_path = os.path.join(BASE_DIR, 'fudamai.log')
def fudamai_log(logger_name='FUDAMAI_LOG', log_file=log_path, level=logging.DEBUG):
    # 创建 logger对象
    logger = logging.getLogger(logger_name)  # 返回一个logger对象并指定名称
    logger.setLevel(level)  # 添加等级

    # 创建控制台 console handler。对象
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # 创建文件 handler。对象
    fh = logging.FileHandler(filename=log_file, encoding='utf-8')

    # 创建 formatter。格式化对象
    formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(name)s %(levelname)s %(message)s')

    # 添加 formatter
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 把 ch， fh 添加到 logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


def main():
    log = fudamai_log()
    log.info('运行信息')

if __name__ == "__main__":
    main()


