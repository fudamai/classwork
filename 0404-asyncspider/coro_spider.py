#! python
# -*- coding:utf-8 -*-
# Author:fudamai
# async_spider.py

"""异步爬虫，抓取指定页面的所有连接地址
"""

import asyncio
import os
import re
import random
import string
from bs4 import BeautifulSoup 
from multiprocessing import Process, Pool
from concurrent.futures import ProcessPoolExecutor
import aiohttp


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

urls = [
    'https://www.vmall.com/list-291',
    'http://baidu.com',
    'http://taobao.com',
    'http://alibaba.com',
    'http://v.qq.com'
]

def make_temp_name(url, count=5, f='.jpg'):
    """重命名，随机算法
    count名称长度，f后缀名
    """
    # return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(count)]) + f
    name = url.split('://')
    return name[1].split('.com')[0] + f


async def download_html(url):
    "下载HTML"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            html = await resp.text()
        return html


async def find_url(url):
    "找到HTML中的URL,并保存为文件"
    html = await download_html(url)
    soup = BeautifulSoup(html)
    url_href = []
    for link in soup.find_all('a'):
        if link.get('href'):
            url_href.append(link.get('href'))
    filename = os.path.join(BASE_DIR, make_temp_name(url, f='.txt'))
    with open (filename, 'w') as f:
        for link in url_href:
            if re.findall('http', link):
                f.write(link)


async def async_spider():
    "异步爬虫"
    tasks = [find_url(url) for url in urls]
    await asyncio.gather(*tasks)


async def process_pool():
    "启动进程池"
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as executor:
        await loop.run_in_executor(executor, async_spider)

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_spider())
    loop.close()
    

if __name__ == '__main__':
    main()
    # process_pool()
