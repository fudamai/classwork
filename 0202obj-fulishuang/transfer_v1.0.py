#! python
# -*- coding:utf-8 -*-
# Author:fudamai


"""
单位转换器，处理温度、长度、货币的转换
用户选择命令，输入待处理的数据
"""


menu = {
    '命令':'对应功能',
    'CtoF':'摄氏度转华氏度',
    'FtoC':'华氏度转摄氏度',
    'KMtoMI':'公里转英里',
    'MItoKM':'英里转公里',
    '$to￥':'美元兑人民币',
    '￥to$':'人民币兑美元',
    'quit':'退出程序'
}
class Transfer:
    "处理输入和输出"
    def __init__(self, turn, num):
        self.turn = turn
        self.num = num

    def clean(self):
        "格式化用户输入的数据"
        try:
            self.choose = (self.turn).lower()  # 将输入的方法选择转为小写
            self.int_num = float(self.num)  # 将输入数字格式化为浮点数
        except ValueError as VE:
            print('数据不是纯数字', VE)

    def trans(self):
        "根据输入，选择功能并处理数据"
        self.clean()
        if self.choose == 'ctof':            
            Temperature.ctof(self.int_num) 
        elif self.choose == 'ftoc':
            Temperature.ftoc(self.int_num)
        elif self.choose == 'kmtomi':
            Length.kmtomi(self.int_num)
        elif self.choose == 'mitokm':
            Length.mitokm(self.int_num)
        elif self.choose == '$to￥':
            Money.rmbtodol(self.int_num)
        elif self.choose == '￥to$':
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
    "程序入口，功能选择，数据输入"
    print('欢迎使用单位转换器'.center(30, '-'))
    for k, v in menu.items():
        print(k,v) 

    while True:
        turn = input('请选择功能：').strip()
        if turn == 'quit':
            break
        num = input('请输入待处理的数据(不需带单位)：').strip()
        try:
            Transfer(turn, num).trans() 
        except Exception:
            print('输入数据格式不正确。')


if __name__ == "__main__":
    main()