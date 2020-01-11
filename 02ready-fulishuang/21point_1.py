#! python
# -*- coding:utf-8 -*-
# Author:fudamai



# 1点游戏
# 两个玩家，游戏开始先输入名字
# 用字典保存每个玩家信息：姓名，获胜次数
# 电脑随机产生两个数，每个玩家轮流才一个数，与电脑随机产生的两个数求和，最接近21点的获胜。
# 每轮结束显示玩家信息
# 按q 退出游戏

# users = {'user1':{'win':0},'user2':{'win':0}}
users = {}
user1_win = 0
user1_fail = 0
user2_win = 0
user2_fail = 0

# 1.导入标准库
import random


print('21点游戏'.center(30,'-'))
target = 21

# 输入玩家的名字
user1 = input('请输入玩家一的名字：')  # 将输入名字放在循环外，规避重新输入
user2 = input('请输入玩家二的名字：')
print(f'玩家：{user1},{user2}')
users[user1] ={'win':user1_win, 'fail':user1_fail}
users[user2] ={'win':user2_win, 'fail':user2_fail}  # 保证每次数据保存正确，引入变量 

turnout = input('是否开始游戏是（y）/否（q）：')

while True:    

    if turnout == 'q':
        print('即将退出游戏。')
        break
    else:
        
        # 产生两个随机数
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)

        # 玩家输入数字
        # 玩家输入数字与随机数相加
        user1_guess = input(f'请{user1}输入一个数字：')
        user2_guess = input(f'请{user2}输入一个数字：')
        user1_sum = num1 + num2 + int(user1_guess)
        user2_sum = num1 + num2 + int(user2_guess)
        print(f'玩家{user1}的最终答案是：{user1_sum}。玩家{user2}的最终答案是：{user2_sum}')

        if abs(user1_sum - 21) < abs(user2_sum - 21):
            print(f'{user1_sum}', f'{user2_sum}')
            print(f'{user1} win')
            user1_win += 1  # 键必须在玩家输入名字时保存
            user2_fail += 1
        elif abs(user1_sum - 21) == abs(user2_sum - 21):
            print('平局')
        else:
            print(f'{user1_sum}',f'{user2_sum}')
            print(f'{user2} win')
            user2_win += 1
            user1_fail += 1    

        print(f'随机数是{num1},{num2}')
        # 重新对字典的值进行赋值
        users[user1] ={'win':user1_win, 'fail':user1_fail}
        users[user2] ={'win':user2_win, 'fail':user2_fail} 

        # 保存玩家信息
        for k, v in users.items():
            print(k,v)        

        turnout = input('是否开始游戏：是（y）/否（q）')

    