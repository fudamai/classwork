#! python
# -*- coding:utf-8 -*-
# Author:fudamai


"""给定商品评论链接，提取评论
"""

import json
import csv
import re
import time
import os
from urllib.parse import urlparse
from datetime import datetime, timedelta
import requests
from requests.exceptions import RequestException

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Throttle:
    """阀门类，对相同域名的访问添加延迟时间，避免访问过快
    """
    def __init__(self, delay):
        self.delay = delay  # 声明延迟
        self.domains = {}  # 用字典保存访问某域名的时间

    def wait(self, url):
        """对访问过得域名添加延迟时间
        """
        domain = urlparse(url).netloc  # 找到原始域名
        last_accessed = self.domains.get(domain)  # 获取最后的访问时间
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
            # 取访问的间隔时间
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.now
    

class Downloader:
    """下载类，根据URL返回内容
    """
    def __init__(self, headers=None, num_retries=3, proxies=None, delay=3, timeout=30):
        self.headers = headers
        self.num_retries = num_retries
        self.proxies = proxies  # 代理
        self.throttle = Throttle(delay)
        self.timeout = timeout  # 超时等待

    def download(self, url, is_json=False):
        """下载json文件或HTML文件
        """
        print('下载页面：', url)
        self.throttle.wait(url)  # 启用延迟
        try:
            response = requests.get(url, headers=self.headers, proxies=self.proxies, timeout=self.timeout)
            print(response.status_code)  # 打印响应的http状态码
            if response.status_code == 200:
                if is_json:
                    return response.json()
                else:
                    return response.content
            return None
        except RequestException as e:
            print('error:', e.response)
            html = ''
            if hasattr(e.response, 'status_code'):  # 判断是否是request错误
                code = e.response.status_code
                print('error code:', code)
                if self.num_retries > 0 and 500 <= code < 600:
                    # 遇到5xx错误就重试
                    html = self.download(url)
                    self.num_retries -= 1
            else:
                code = None
        return html


class Recorder:
    """记录类，根据不同保存类型使用相应方法。
    定义回调函数，可直接调用类方法
    """
    def __init__(self, save_type='csv'):
        self.save_type = save_type

    def __call__(self, filename, fields, all_list):
        # 增加魔法方法，定义类时自动调用此方法
        if hasattr(self, self.save_type):
            func = getattr(self, self.save_type)
            return func(filename, fields, all_list)
        else:
            return {'status':1, 'statusText': 'no record function'}
    
    def csv(self, filename, fields, all_list):
        """将filename保存为CSV文件
        """
        try:
            with open(filename, 'w', newline='') as f:
                # 指定newline规避文件写入时多空行问题
                writer = csv.writer(f)
                writer.writerow(fields)
                for row in all_list:
                    writer.writerow(row)
            return {'status': 0, 'statusText': 'cav saved'}
        except Exception as e:
            print(e)
            return {'status': 1, 'statusText': 'cav error'}


class ItemCommenSpider:
    """抓取商品评价
    """
    def __init__(self, headers=None, num_retries=3, proxies=None, delay=3, timeout=30):
        self.download = Downloader(headers,num_retries, proxies, delay, timeout)

    def get_comment_by_json(self, url):
        """抓取json格式的评价信息，包含完整评论
        """
        data = self.download.download(url, is_json=True)
        comments = data['comments']
        data_list = []
        for c in comments:
            row = []
            row.append(c['creationTime'])
            row.append(c['userClientShow'])
            row.append(c['userLevelName'])
            row.append(c['productSize'])
            row.append(c['productColor'])
            row.append(c['productSales'][0]['saleValue'])
            row.append(c['content'])
            data_list.append(row)
        return data_list

    def fetch_data(self, url, filename, page_start, page_end, page_offset, callback=None):
        """手动输入获取评论的起止页码，根据URL获取评论并保存至filename
        """
        all_list = []
        for page in range(page_start, page_end, page_offset):
            data_list = self.get_comment_by_json(url.format(page))  # 自动填入评论的页码
            all_list += data_list  # 合并各页的评论到一个列表
            print(f'完成第{page}')

        if callback:
            # 当callback不为None时，调用callback
            # 定义callback
            # callback参数固定，callback名根据调用fetch_data
            callback(filename, ('creationTime', 'userClientShow', 'userLevelName', 'productSize', "productColor", 'saleValue', "content") , all_list)



def main():
    headers = {
        'User-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        "referer": "https://passport.jd.com"
    }
    # url = 'https://sclub.jd.com/comment/productPageComments.action?productId=6946605&score=1&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1'  # P20评论的地址
    url = input('请输入产品的评论地址：').strip()
    spider = ItemCommenSpider(headers=headers)
    spider.fetch_data(url, 'db.csv', 0, 30, 1, Recorder('csv'))


if __name__ == '__main__':
    main()
      