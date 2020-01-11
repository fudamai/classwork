#! python
# -*- coding:utf-8 -*-
# Author:fudamai


"""
单位转换器，处理温度、长度、货币的转换
用户直接输入数据，程序自行判断需要转换的单位，并分离出需处理的数据
这里使用正则判断、分离数据，用户只需输入想处理的信息。
"""
import re


class Transfer:
    "处理输入和输出"
    def __init__(self, enter):
        "构造方法，定制实例的属性"
        self.enter = enter
        

    def clean(self):
        "格式化用户输入的数据。根据正则的贪婪匹配特性，使用正则判断输入数据的格式。再使用正则分离出需要的部分。"
        try:
            all = re.compile(r'^\d*\D{1,}$')
            c_re = re.compile(r'\D{1,2}$')  # 不加结束符，20kmmm也能处理
            in_re = re.compile(r'^\d*')

            self.enter == all.findall(self.enter)[0]  # 判断输入格式是否符合正则
            self.choose = (c_re.findall(self.enter)[0]).lower()  # 将单位转为小写
            self.int_num = float(in_re.findall(self.enter)[0])
        except Exception as e:
            print('数据格式不正确', e)


    def trans(self):
        "根据输入，选择功能并处理数据"
        # float的参数不能为字符串，空字符串也不可以。规避报错，直接判断self.center
        if self.enter == 'quit':
            return 'q'

        self.clean()
        
        if self.choose == 'c':            
            Temperature.ctof(self.int_num) 
        elif self.choose == 'f':
            Temperature.ftoc(self.int_num)
        elif self.choose == 'km':
            Length.kmtomi(self.int_num)
        elif self.choose == 'mi':
            Length.mitokm(self.int_num)
        elif self.choose == '$':
            Money.rmbtodol(self.int_num)
        elif self.choose == '￥':
            Money.doltormb(self.int_num)
        else :
            print('待开发功能！')       


class Temperature:
    "温度转换类，可执行摄氏度与华氏度的转换"
    
    @staticmethod
    def ctof(temp):
        "摄氏度转华氏度"
        result = 32 + 1.8*temp  
        print(f'摄氏度转华氏度结果为 {result}')
    

    @staticmethod
    def ftoc(temp):
        "华氏度转摄氏度"
        result = (temp - 32)/1.8 
        print(f'华氏度转摄氏度结果为 {result}')
    pass


class Length:
    "长度单位转换，处理千米与英里，米与英尺的相互转换"
    
    @staticmethod
    def kmtomi(temp):
        "公里转英里"
        result = 0.62*temp  
        print(f'公里转英里结果为 {result}')


    @staticmethod
    def mitokm(temp):
        "英里转公里"
        result = 1.61*temp 
        print(f'英里转公里结果为 {result}')


class Money:
    "货币单位转换，处理人民币与美元、日元、卢布的相互转换"
    
    @staticmethod
    def rmbtodol(temp):
        "人民币兑美元"
        result = 7*temp          
        print(f'人民币兑美元结果为 {result}')


    @staticmethod
    def doltormb(temp):
        "美元兑人民币"
        result = 0.14*temp  
        print(f'美元兑人民币结果为 {result}')


def main():
    print('欢迎使用单位转换器'.center(30, '-'))
    
    while True:
        enter = input('请输入内容：')
        if Transfer(enter).trans() == 'q':
            break
       


if __name__ == "__main__":
    main()