#! python
# -*- coding:utf-8 -*-
# Author:fudamai


"""TODO:
完成调用抓取评论、差评分析
添加自动命名
"""

import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from core import analysis
from core import comment_hunter


def choose():
    """选择功能，如：评论爬取、评论分析
    """
    menu = {
        '0':'评论抓取',
        '1':'评论分析'
    }

    print('欢迎使用爬虫'.center(30, '-'))
    for k, v in menu.items():
        print(k ,v)

    try:
        num = input('根据需求输入对应的数字：').strip()
        if num == '0':
            print('评论抓取。')
            url = input('请输入产品的评论地址：').strip()
            filename = input('输入保存评论的文件名（不带后缀）：').strip()
            headers = {
                'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
                "referer": "https://passport.jd.com"
            }
            spider = comment_hunter.ItemCommenSpider(headers=headers)
            spider.fetch_data(url, f'{filename}.csv', 0, 30, 1, comment_hunter.Recorder('csv'))
        elif num == '1':
            print('差评分析。')
            print('请将文件放入 ./db 文件夹下')

            filename = input('请输入待处理文件名（不带后缀）：')
            parses = analysis.Analysis()
            words = parses.get_bad_words( f'{filename}.csv')
            for k, v in words.items():
                print(k, '-->', len(v), v)
        else:
            print('请输入正确的代码')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    choose()