#! python3.8
# -*- coding:utf-8 -*-
# author:fudamai
# spider.py

"""
爬取百度新冠肺炎页面
从指定的统一资源定位器下载HTML
分析HTML，找到指定的数据。这里是json文件
保存文件，将日期添加到文件名中
"""

import os
import json
import datetime
import requests
from bs4 import BeautifulSoup


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)


def filename_maker():
    """自动生成文件名
    文件名：'virusdata' + <date> + <.json>
    """
    date = datetime.date.today().isoformat()
    filename = 'virusdata' + date + '.json'
    return filename

def get_data_from_url(url):
    response = requests.get(url)

    soup_all = BeautifulSoup(response.content, 'html.parser')
    virus_data = soup_all.find(type='application/json').string
    # print(json.loads(virus_data))

    filepath = os.path.join(BASE_DIR, 'db', filename_maker())
    with open(filepath, 'w',encoding='utf-8') as f:
        json.dump(json.loads(soup_all.find(type='application/json').string), f, ensure_ascii=False)

    return virus_data


def main():
    url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1"
    get_data_from_url(url)

if __name__ == '__main__':
    main()