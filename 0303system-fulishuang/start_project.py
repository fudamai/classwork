#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# start_project.py
# 初始化工程目录
# author: De8uG


import os
import sys


__author__ = 'De8uG'
path = os.path.dirname(os.path.abspath(__file__))


def start_project():
    # 从命令行参数取工程名， 默认为de8ug_demo
    project_name = 'fudamai_demo'
    if len(sys.argv) > 1:
        project_name = sys.argv[1]

    # 创建目录, readme, __init__文件
    folders = ['bin', 'conf', 'core', 'db', 'log']
    for folder in folders:
        folder_path = os.path.join(path, project_name, folder)
        print(folder_path)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # readme
        with open(os.path.join(path, project_name, 'readme.md'), 'w') as f:
            f.write('# ' + project_name + '\n\n')
            f.write('> Author: ' + __author__ + '\n')
        # add init file
        with open(os.path.join(path, project_name, folder, '__init__.py'), 'w'):
            pass


def main():
    start_project()

if __name__ == '__main__':
    main()