#! python
# -*- coding:utf-8 -*-
# Author:fudamai


import os
import sys
import json
from docx import Document

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import word_util
from core import image_util
from core import auth
from core import log_fun


@auth.Auth
class Choose:
    """打印可执行的功能，并选择
    """
    def __init__(self, user_info):
        self.user_info = user_info
        self.type = self.user_info['type']
        self.menu = self.user_info['operation']
        self.logger = log_fun.fudamai_log(logger_name='main_logger')
    
    def select(self):
        """选择功能
        """
        print(f'用户类型:{self.type}')
        self.logger.info(f'用户登录，类型{self.type}')
        print('可使用功能（代码:功能）：')
        for i, m in enumerate(self.menu):
            print(i, m)
        try:
            if len(self.menu) == 0:
                print('没有可使用功能，请联系管理员。')
            else:
                num = input('请输入功能代码：').strip()
                c = self.menu[int(num)]
                if c in self.menu[int(num)]:
                    func = getattr(self, c)
                    func()
                else:
                    print('请输入正确的代码')
                    self.logger.info('用户输入无法执行指令')
        except Exception as e:
            print(e)
            self.logger.error(f'程序报错：{e}')
    
    def weighting(self):
        """给用户添加操作权限
        """
        username = input('输入用户名：').strip()
        conf = auth.Auth(self).load(username)  # 载入json格式的配置文件
        if all([conf, self.is_admin()]):
            try:
                func = input('输入添加的功能：').strip()
                conf['operation'].append(func)
                self.logger.info(f'为{username}添加{func}功能')
                print(conf)
                self.save_json(conf, username)
                self.logger.error(f'管理员为用户添加功能：{func}')
            except Exception as e:
                print(e)
                self.logger.critical(f'为用户添加功能时报错{e}')
        else:
            self.weighting()
     
    def blacklist(self):
        """将指定用户加入黑名单
        """
        print('进行添加黑名单操作')
        username = input('输入用户名：').strip()
        conf = auth.Auth(self).load(username)
        if all([conf, self.is_admin()]):
            try:
                able = input('输入用户状态（1，正常。0，黑名单）：').strip()
                conf['enabled'] = int(able)
                self.save_json(conf, username)
                self.logger.warning(f'将{username}拉入黑名单')
            except Exception as e:
                print(e)
                self.logger.error('进行拉黑用户时出错')

    def is_admin(self):
        """判断是否是管理员
        """
        if self.type == 'admin':
            return True
        else:
            print('不是管理员账户，不能进行此操作')
            return False

    def save_json(self, dic, username):
        """输入字典及用户名，将字典保存为json文件，文件名为 用户名.json
        """
        json_path = os.path.join(BASE_DIR, 'conf', f'{username}.json')
        with open(json_path, 'w') as f:
            json.dump(dic, f)
            self.logger.info(f'保存{username}的json文件')

    def word_util(self):
        """实现写入word文件操作
        """
        self.logger.info('进行写入Word文件操作')
        print('欢迎使用Word'.center(30,'-'))
        menu ={
            'title':'选择输入标题',
            'subtitle':'选择输入副标题',
            'para':'选择输入正文',
            'save':'输入文件名并保存',
            'quit':'关闭程序'
        }
        for k,v in menu.items():
            print(f'{k}:{v}')

        w_type = input('请根据需要输入命令：')
        in_doc = Document()  # 在类中指定实例会导致每次循环生成新的实例，调用save时保存的是空文件
        while w_type: 
            if w_type == 'quit':
                print('即将关闭程序')
                break
            
            text= input('输入文本：')
            word_util.Word_util(text=text, in_doc=in_doc, w_type=w_type).add_text()  # 使用关键字参数
            w_type = input('请根据需要输入命令：')

    def image_util(self):
        """实现图片操作
        """
        self.logger.info('进行图片操作')
        menu = {
            'th':'生成缩略图',        
            'rt':'旋转图像，可以镜像翻转',        
            'rg':'根据输入的坐标裁剪图像',
            'nte':'将目录文件夹中图片名整理保存至Excel，此功能可输入绝对路径',
            'quit':'退出程序'
        }
        print('请将需处理的图片放入db目录下')
        im_name = input('请输入目标路径名：')
        image = image_util.ImageSystem(im_name)
        for k, v in menu.items():
            print(k, v)
        
        while True:
            choose = input('请输入要执行的功能：').strip().lower()     
            if choose == 'tb':
                image.thumbnail()
                image.logger.info('调用thumbnail方法')
            elif choose == 'rt':
                angle = input('请输入旋转角度：')
                mirror = input('输入镜像规则（n键跳过）')
                image.rotate(int(angle), mirror)
                image.logger.info('调用rotate方法')
            elif choose == 'rg':
                image.region()
                image.logger.info('调用region方法')
            elif choose == 'nte':
                image.name_to_excel()
                image.logger.info('调用name_to_excel方法')
            elif choose == 'quit':
                image.logger.info('调用quit方法')
                print('即将退出')
                break
            else:
                print('待开发功能')           
                image.logger.warning('未指定功能代码')        


def main():
    
    while True:

        start = input('是否启动程序（Y/N）：').strip().lower()
        if start == 'n':
            break
        elif start == 'y':
            m = Choose()
            m.select()
        else:
            print('请输入正确参数。')


if __name__ == '__main__':
    main()
