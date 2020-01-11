#! python
# -*- coding:utf-8 -*-
# Author:fudamai
# async_spider.py

"""异步爬虫，抓取指定页面的所有连接地址
"""

import asyncio
import os
import re
import logging
import sys
from bs4 import BeautifulSoup 
from concurrent.futures import ProcessPoolExecutor
import requests


urls = [
    'https://www.vmall.com/list-291',
    'http://baidu.com',
    'http://taobao.com',
    'http://alibaba.com',
    'http://v.qq.com'
]


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(level=logging.DEBUG, format='%(processName)-10s: %(message)s')


class Mulipro_Spider:
    def __init__(self, url, dirname):
        self.url = url
        self.dirname = dirname

    def make_temp_name(self, url, f='.jpg'):
        """重命名,f后缀名。将网页名设为文件名
        """
        name = url.split('://')
        return name[1].split('.com')[0] + f

    def download_html(self, url):
        "下载HTML"
        logging.debug('下载HTML')
        r = requests.get(url)
        print(r.status_code)
        return r.text

    def find_url(self, url):
        "找到HTML中的URL,并保存为文件"
        html =self.download_html(url)
        soup = BeautifulSoup(html)
        url_href = []
        for link in soup.find_all('a'):
            if link.get('href'):
                url_href.append(link.get('href'))
        filename = os.path.join(self.dirname, self.make_temp_name(url, f='.txt'))
        with open (filename, 'w') as f:
            for link in url_href:
                if re.findall('http', link):
                    f.write(link)
        logging.debug('提取出URL并保存')

    async def process_pool(self, url_pool):
        "进程池"
        loop = asyncio.get_running_loop()
        with ProcessPoolExecutor() as executor:
            for url in url_pool:
                future = await loop.run_in_executor(executor, self.find_url, url)
        logging.debug('启动进程池')

    def run(self):
        logging.debug('启动多进程爬虫')
        asyncio.run(self.process_pool(self.url))
    
def help():
    print("""usage:
    -h or --help,获取帮助
    -u URL,抓取给定URL页面的全部链接
    """)


def main():
    
    if len(sys.argv) == 1:
        spider = Mulipro_Spider(urls, BASE_DIR)
        spider.run()
    elif sys.argv[1] in {'-h', '--help'}:
        help()
    elif sys.argv[1] in {'-u', '--url'}:
        try:
            url_in = []
            url_in.append(sys.argv[2])
            print(url_in)
            spider = Mulipro_Spider(url_in, BASE_DIR)
            spider.run()
        except Exception as e:
            print(e, '请输入正确的URL')

if __name__ == '__main__':
    main()