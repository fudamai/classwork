#! python
# -*- coding:utf-8 -*-
# Author:fudamai


"""给定评论数据，分辨出差评
"""

import csv
import re
import os
import requests
import jieba
import jieba.analyse
from core import log_fun
from core.comment_hunter import Recorder


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
stop_words = os.path.join(BASE_DIR, 'core', 'stop_words.txt')


        
class Analysis:
    def __init__(self, stop_words=stop_words):
        self.logger = log_fun.fudamai_log()
        self.stop_words = stop_words

    def get_all_text(self, filename):
        """给定CSV格式评论，取出所有评价句子
        """
        comment_list = []
        try:
            with open(filename) as f:
                rows = csv.reader(f)  # 打开CSV文件
                for row in rows:
                    one_comment = row[-1]
                    comment_list.append(one_comment)
                    self.logger.info('CSV文件打开成功，添加到列表')
        except Exception as e:
            print('打开CSV文件时报错', e)
            self.logger.warning(f'打开CSV文件时报错{e}')
        self.logger.info('输出评价组成的列表')
        return ''.join(comment_list[1:])  # 排除第一行（表头）

    def cut_text(self, all_text):
        """找到评价中重要关键词
        """
        try:
            jieba.analyse.set_stop_words(self.stop_words)  # 添加停止词
            text_tags = jieba.analyse.extract_tags(all_text, topK=30)  # 寻找前30位关键词
            
        except Exception as e:
            print('寻找关键词时报错', e)
            self.logger.warning(f'寻找关键词时报错{e}')
        self.logger.info('输出关键词')
        return text_tags

    def get_bad_words(self, filename):
        """根据关键词找到对应句子,输出到控制台，保存为文件
        """
        try:
            comment_path = os.path.join(BASE_DIR, 'db', filename)
            all_text = self.get_all_text(filename=comment_path)
            text_tags = self.cut_text(all_text=all_text)
            words = {}
            for tag in text_tags:
                tag_re = re.compile(f'(\w*{tag}\w*)')
                words[tag] = tag_re.findall(all_text)
            bad_words_filename, bad_words_path = self.autoname(filename, '1')
            Recorder().csv(bad_words_path, ('关键词','次数','详细内容'), self.to_list(words))
            print(f'关键语句已保存为文件，文件名:{bad_words_filename}')
            self.logger.debug('将关键语句保存为文件')
        except Exception as e:
            print(e)
            self.logger.warning(f'查找关键语句报错{e}')
        self.logger.info('输出关键语句')
        return words

    def autoname(self, name, pre):
        """自动命名,传入文件名及pre
        ,将pre作为后缀加入文件名
        """
        re_name = re.compile('\.\w{0,4}?$')
        match = re_name.search(name)
        try:
            new_name = re_name.sub(f'-{pre}{match.group()}', name)
            self.logger.info('重命名')
            target_name = os.path.join(BASE_DIR, 'db', new_name)
            return new_name, target_name
        except Exception as e:
            self.logger.error(f'{e}文件后缀名不匹配')
            print('文件后缀名不匹配')


    def to_list(self, words):
        """将字典转换为列表
        """
        words_list = []
        try:
            for k,v in words.items():
                words_list.append([k, len(v), v])
        except Exception as e:
            print(e)
            self.logger.warning(f'关键语句转化为列表出错{e}')
        self.logger.info('将关键语句转化为列表')
        return words_list

def main():
    # all_text = get_all_text('db.csv')
    # text_tags = cut_text(all_text)
    # print(text_tags)
    comment_path = os.path.join(BASE_DIR, 'db', 'db.csv')
    parses = Analysis()
    words = parses.get_bad_words(comment_path)
    for k, v in words.items():
        print(k, '-->', len(v), v)

if __name__ == '__main__':
    main()