#! python
# -*- coding:utf-8 -*-
# Author:fudamai


"""
备忘录小程序
模式S(sentence)，输入一定格式语句，程序分割时间与事件并保存
模式W(Word)，按指示输入输入日期、事件、耗时，程序将输入分类保存
保存完成，打印记录信息
"""


from color_me import ColorMe
ex_time = ColorMe('明天早上八点').red()
ex_thing = ColorMe('提醒我带钥匙').green()
# 将提示分段，并使用不同颜色标记

print('欢迎使用51备忘录'.center(30, '-'))
menu = {'S':'输入语句自动识别','W':'按提示输入详细信息'}

all_memo = []
is_add = True
all_time = 0

while is_add:
    for k, v in menu.items():
        k_c = ColorMe(k).green()  # 用色彩标记字典的键
        print(f'{k_c}:{v}')
    mode = input('请按需求选择模式：').casefold()
    print('请输入备忘信息：')

    if mode == 's':
        print('输入一段话。示例：' + ex_time + ex_thing)
        words = input('请输入：').strip()
        in_alarm = words[0: words.find('点')+1]
        in_thing = words[words.find('点')+1: ]
        print ('代办列表'.center(30,'-'))
        memo = {}
        memo['alarm'] = in_alarm
        memo['thing'] = in_thing
        all_memo.append(memo)
    
    elif mode == 'w':
        in_date = input('日期：')
        in_thing = input('事件：')
        in_time = input('用时：')
        print('待办列表'.center(30, '-'))
        one = {}
        one['date'] = in_date
        one['thing'] = in_thing
        one['time'] = in_time
        all_memo.append(one)
        all_time += int(in_time)

    num = 0
    for m in all_memo:
        num += 1
        print('%s:%s' %(num, m))

    print(f'共{len(all_memo)}条待办事项, 总时长：{all_time}。', end='')
    print('（y：继续添加，n: 退出）')
    is_add = input().strip() == 'y'    
