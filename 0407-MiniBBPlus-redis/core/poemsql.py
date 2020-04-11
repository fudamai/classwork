#! python3.8
# -*- coding:utf-8 -*-
# author:fudamai
# poemsql.py
# creat, query, delete
# demo for ueing sqlalchemy

"""创建数据库时，注意编码指定问题
"""
import datetime
import random
from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship,outerjoin
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Authors(Base):
    __tablename__ = "authors"

    id = Column('author_id', Integer, primary_key=True)  # 定义第一列的id。定义主键
    name = Column('name', String(50))
    city = Column('city', String(50))

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.city}'
        # return "<>"


class Article(Base):
    __tablename__ = "articles"

    id = Column('article_id', Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.author_id'))
    title = Column('title', String(20))
    content = Column('content', String(180))
    comment = Column('comment', String(50))
    create_date = Column('create_date', String(10))

    authors = relationship("Authors", back_populates="articles")  # 建立关联

    def __repr__(self):
        return f'{self.id}, {self.title}, {self.content}, {self.comment}, {self.create_date}'


Authors.articles = relationship("Article", back_populates="authors", order_by=Authors.id)  # 建立一对多关联

class Sql_tool():
    """SQL操作工具包，创建表，创建与数据库的会话
    往表单添加信息时，先add，再commit
    """
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:fristmaria@localhost/poem', echo=True)  # 指定默认数据库。echo，设置日志
        self.session = self.mk_session()

    def create_table(self):
        """创建数据库表
        """
        Base.metadata.create_all(bind=self.engine)  # 创建只需一次

    def mk_session(self):
        """创建与数据库的会话
        """
        DBSession = sessionmaker(bind=self.engine)
        return DBSession()

    def add_author(self, name, city=None, id=None):
        """往author数据库插入数据
        需指定id，name，city
        id可无需指定，自动生成
        """
        author = Authors()
        author.name = name
        author.city = city
        
        if id == None:
            author.id = randomid(self.session, Authors)
        else:
            author.id = au_id_make(id)
        print('返回新建的Author对象')
        return author

    def add_article(self, title, content, author_name, comment=None, date=None, id=None):
        """往article数据库插入数据
        需指定id，author_id，title, content, comment, create_date
        id可无需指定，自动生成
        """
        poem = Article()
        poem.title = title
        poem.content = content
        poem.comment = comment
        poem.create_date = datetime.date.today().isoformat()
        if id == None:
            poem.id = randomid(self.session, Article)
        else:
            poem.id = p_id_make(id)
        poem.authors = author_name
        return poem

    def commit(self, table):
        """接收表单，将表单添加到session，提交
        """
        # session = DBSession()
        self.session.add(table)  # 添加实例到会话中
        self.session.commit()  # 提交数据

def randomid(session, table_class):
    """自动生成9位数字，整形成可用id，遍历表单。
    若表单内无重复id，id可用
    """
    num = random.randrange(1,99999999)  # 八位整数。添加文章时，id左数第二位大于一时报错Out of range value for column 'article_id' at row 1")
    # num = 1000000001
    if table_class == Authors:
        id_num = au_id_make(num)
    elif table_class == Article:
        id_num = p_id_make(num)
    result_list = session.query(table_class.id).filter(table_class.id == id_num).all()
    print(result_list)
    while result_list:
        id(session, table_class)
    else:
        return id_num

def au_id_make(id):
    """作家id生成，首位为1"""
    id = str(id)
    if len(id) > 10:
        print('长度过长。id为长度限制在十位以内的纯数字。')
    else:
        id = '1' + id.rjust(9, '0')
        return int(id)

def p_id_make(id):
    """"诗id生成，首位为2"""
    id = str(id)
    if len(id) > 10:
        print('长度过长。诗id为长度限制在十位以内的纯数字。')
    else:
        id = '2' + id.rjust(9, '0')
        return int(id)

def date(year, mounth, day):
    """输出指定格式日期
    """
    date_str = (year, mounth, day)
    date = datetime.date(date_str).isoformat()
    return date

def show(session, class_name=None, mode=1):
    """默认展示所有数据,mode=1
    根据输入类名展示表单所有数据
    """
    if mode == 1:
        # author_list = session.query(Authors).join(Article.authors).all()
        result_list = session.query(Authors.name, Article.content).outerjoin(Authors.articles)  # 外连接，展示作者名与此作者全部的诗内容
        return result_list
    if mode ==2:
        result_list = session.query(class_name)
        return result_list

def auto_add(title, content, author_name):
    """输入文章名（title），内容（content），作者（author.name）
    自动填入表单，并提交入数据库
    """
    author = Sql_tool().add_author(author_name)
    # if author == '1':
    #     author = session.query(Authors).filter(Authors.name == author_name).[0]
    author.articles = [Sql_tool().add_article(title, content, author)]
    Sql_tool().commit(author)
    # Sql_tool().commit(article)

def delete(session, id):
    """根据文章id，删除文章
    """
    session.query(Article).filter(Article.id == id).delete(synchronize_session='fetch')
    session.commit()


def main():
    # 添加有联系关系的表单时，作者如果没有添加，可与诗建立连接后，绑定提交。
    # 若已添加作者，需使用query方法返回author对象，再与诗绑定提交
    tool = Sql_tool()
    session = Sql_tool().mk_session()
    table = tool.add_author("test1")
    table.articles = [
        Article(id=1, title='首诗', content='第一首诗'),
        Article(id=2, title='首诗', content='第二首诗'),
        Article(id=3, title='首诗', content='第三首诗'),
        Article(id=4, title='首诗', content='第四首诗')
    ]

    session.commit()

    # result = session.query(Authors.name).filter(Authors.name == 'test2')
    # for 
    # print(result)

    # q = session.query(Authors.name).filter(Authors.name == 'test2')
    # print(q.all())
    # for i in q.all():
    #     if not 'test2' in i:
    #         judge = True
    #     else:
    #         judge = False
    #     print(judge)
    # if len(q.all()) > 0:
    #     judge = True
    # else:
    #     judge = False
    # print(judge)
    # result1 = session.query(Authors).filter(Authors.name == '崔护')
    # print(type(result1))
    # print(result1)
    # for i in result:
    #     print(i)
    # bool = '崔护' in result
    # print(bool)
    # for i in show(session):
    #     print(i)

    # session.query(Authors).filter(Authors.name == "陈子昂").delete(synchronize_session='fetch')
    # session.commit()
    # commit(table, session)
    
    # delete(session, 2000000001)

    # print(id(session, Authors))
    # auto_add('幽州台歌', '望天地之悠悠，独怆然而涕下','陈子昂')

    pass

if __name__ == '__main__':
    main()