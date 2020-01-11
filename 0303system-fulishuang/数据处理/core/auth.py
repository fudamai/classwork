#! python
# -*- coding:utf-8 -*-
# Author:fudamai


import json
import os
from core import log_fun

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


dic = {
    'username': '',
    'password': '',
    'type': 'user',
    'operation': [],
    'enabled': 1
}

class Auth(object):

    def __init__(self,cls):
        self.login_status = False
        self.__cls = cls
        self.user_info = {}
        self.logger = log_fun.fudamai_log(logger_name='auth_logger')

    def login(self):
        print('请登录'.center(50,'-'))
        try:
            user = input('username:').strip()
            pwd = input('password:').strip()
            json_path = os.path.join(BASE_DIR, 'conf', f'{user}.json')
            if os.path.isfile(json_path):
                self.user_info = self.load(user)
                if self.user_info['password'] == pwd:
                    self.login_status = True
                    self.logger.info('验证密码正确')
                else:
                    print('密码不正确')
                    self.logger.warning('密码不正确')
            else:
                print('用户不存在')
                t = input('是否注册新用户（y/n）：').strip().lower()
                if t == 'y':
                    self.register()
        except Exception as e:
            print(e)

    def __call__(self,*args,**kwargs):
        print('登录状态：',self.login_status)
        if not self.login_status:
            self.login()
            cls = self.__call__(self,*args,**kwargs)
            # 递归检测登录状态
        else:
            cls = self.__cls(user_info=self.user_info)
        self.logger.info('添加登录装饰并返回')
        return cls
    
    def register(self):
        """当未找到用户名对应的json文件时，提供注册
        """
        # TODO:用户名及密码规则设定
        print('注册新用户')
        try:
            user = input('请输入用户名：').strip()
            password = input('请输入密码：').strip()
            dic['username'] = user
            dic['password'] = password
            json_path = os.path.join(BASE_DIR, 'conf', f'{user}.json')
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(dic, f)
                self.logger.info('用户注册成功')
        except Exception as e:
            print(e)

    def load(self, username):
        try:
            json_path = os.path.join(BASE_DIR, 'conf', f'{username}.json')
            with open(json_path, 'r') as f:
                conf = json.load(f)
            self.logger.info('读取用户文件成功')
            return conf
        except Exception as e:
            print('获取用户信息出错',e)
            return None


@Auth
class Memo(object):

    def __init__(self,user_info):
        print('备忘录初始化')
        self.user_info = user_info

    
    def query(self):
        print(f'查询{self.user_info["name"]}的备忘录')



# memo = Memo()
# # 实例化时做装饰器验证
# memo.query()