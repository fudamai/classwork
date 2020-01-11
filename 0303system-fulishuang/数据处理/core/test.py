#! python
# -*- coding:utf-8 -*-
# Author:fudamai


import json
import os
from collections import defaultdict
from functools import wraps


admin_json = {
    "username": "admin",
    "password": "admin",
    "type": "admin",
    "operation": ["crawler", "office", "image"]
}
dic = {
    'username': '',
    'password': '',
    'type': 'user',
    'operation': [],
    'enabled': 1
}


def register():
    """当未找到用户名对应的json文件时，提供注册
    """
    # dic = defaultdict(user_dic)
    user = input('请输入用户名：').strip()
    password = input('请输入密码：').strip()
    dic['username'] = user
    dic['password'] = password
    with open(f'{user}.json', 'w', encoding='utf-8') as f:
        json.dump(dic, f)


def login():
    """提供登录验证
    """
    pass




class Login:
    def __init__(self, filename='log-test.txt'):
        self.filename = filename
        self.username = input('username: ')
        self.password = input('password: ')
        # self.funcname = funcname
    
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kw):
            if(self.check()):
                func(*args, **kw)
            else:
                print('登录失败')
        return wrapper   

    def log(self, func):
        str_log = '函数{}开始运行...'.format(func.__name__)
        with open(self.filename, 'a', encoding='utf8') as f:
            print(str_log)
            f.write(str_log + '\n')
        return True

    def check(self):
        if self.load(self.username):
            conf = self.load(self.username)
            if conf['password'] == self.password:
                return True
            else:
                print('密码不正确')
                return False
        
    def register(self):
        """当未找到用户名对应的json文件时，提供注册
        """
        print('注册新用户')
        # dic = defaultdict(user_dic)
        user = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        dic['username'] = user
        dic['password'] = password
        with open(f'{user}.json', 'w', encoding='utf-8') as f:
            json.dump(dic, f)

    def load(self, username):

        if os.path.isfile(f'{username}.json'):
            with open(f'{username}.json', 'r') as f:
                conf = json.load(f)
            return conf
        else:
            print('用户不存在')
            r = input('是否注册新用户（y/n）：').strip().lower()
            if r == 'y':
                self.register()
                self.check()
            else:
                self.check()


@Login()
def choose():
    print(1)


choose()

# if os.path.isfile('man1.json'):
#     print(1)