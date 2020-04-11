#! python3.8
# -*- coding:utf-8 -*-
# author:fudamai
# admin.py

"""
数据库管理，为server提供接口
"""

import sys
import json
import argparse
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.poemsql import Authors, Article, Sql_tool
# from core.basemq import FubaiMQ
from bin.rabbitmq_pub import fanout_pub


class Admin():
    def __init__(self):
        self.session = Sql_tool().mk_session()
            
    def show(self, class_name=None, mode=1):
        """默认展示所有数据,mode=1
        根据输入类名展示表单所有数据
        输出结果是类对象
        """
        if mode == 1:
            # result = session.query(Authors).join(Article.authors).all()
            result = self.session.query(Authors.name, Article.content).outerjoin(Authors.articles)  # 外连接，展示作者名与此作者全部的诗内容
            print('输出全部内容')
            return result
        if mode ==2:
            result_list = self.session.query(class_name)
            print('输出')
            return result_list

    def query_article_to_json(self, id, mode=1):
        """mode=1时，根据id查询文章
        mode=2时，输出所有文章
        将结果输出为json
        """
        if mode == 1:
            result = self.session.query(Article).filter(Article.id == id)
            # print(result)
            for i in result:
                ar_id = json.dumps({'author':i.authors.name, 'article':{'id':i.id, 'title':i.title, 'content':i.content}}, ensure_ascii=False, separators=(',', ':'), indent=4)
                print(ar_id)
            print('输出指定id的文章')
            return ar_id
        elif mode == 2:
            result = self.session.query(Article)
            article_list = []
            for i in result:
                article_list.append({'id':i.id, 'author':i.authors.name, 'title':i.title, 'content':i.content})
                # print(i.id, i.title, i.content, i.authors.name)
                ar_all = json.dumps({'status':0, 'statusText':'所有文章数据', 'articles':article_list}, ensure_ascii=False, separators=(',', ':'), indent=4)
            print('输出全部文章')
            return ar_all

    def auto_add(self, title, content, author_name):
        """输入文章名（title），内容（content），作者（author.name）
        自动填入表单，并提交入数据库
        """
        author_exist_judge = self.session.query(Authors).filter(Authors.name == author_name).all()
        if author_exist_judge:  # 判断author是否存在。不存在时，author_exist_judge为空列表
            author = self.session.query(Authors).filter(Authors.name == author_name)[0]
        else:
            author = Sql_tool().add_author(author_name)

        article = Sql_tool().add_article(title, content, author)

        self.session.add(article)
        self.session.commit()

        print(f'添加文章 {title} 成功')

    def delete(self, id):
        """根据文章id，删除文章
        """
        self.session.query(Article).filter(Article.id == id).delete(synchronize_session='fetch')
        self.session.commit()
        print(f'删除id为{id}的文章成功。')

def main():
    """命令行：
    '--show'，展示所有数据
    '--add <title> <content> <author>
    '--delete <article_id>' 
    """
    # TODO 添加直接输入SQL命令的模式
    parser = argparse.ArgumentParser("fubai sql功能列表")
    group1 = parser.add_argument_group('group1', '基本命令')
    group1.add_argument('--show', dest='show', action='store_true', help="展示所有的作者及文章")
    group1.add_argument('--add', dest='add', nargs=3, help="自动保存数据，--add <title> <content> <author>")
    group1.add_argument('--delete', dest='delete', nargs=1, help="删除指定id的文章，--delete <article_id>")

    args = parser.parse_args()
    tool = Admin()

    
    if args:
        parser.print_help()
    if args.show:
        result = tool.show()
        print(result.all())
        fanout_pub(json.dumps({'status':0, 'behavior':'show', 'article':result.all()}, ensure_ascii=False), 'show')
    elif args.add:
        title = args.add[0]
        content = args.add[1]
        author_name = args.add[2]
        tool.auto_add(title, content, author_name)
        fanout_pub(json.dumps({'status':0, 'behavior':'add', 'article':{'title':title, 'content':content, 'author_name':author_name}}, ensure_ascii=False), 'add')
    elif args.delete:
        id = args.delete[0]
        tool.delete(id)
        fanout_pub(json.dumps({'status':0, 'behavior':'delete', 'article':result}, ensure_ascii=False), 'delete')


if __name__ == "__main__":
    main()