#! python
# -*- coding:utf-8 -*-
# Author:fudamai
# 51memoV0.34-fu.py


import pickle
import configparser
import os
import sys
import pdf_demo
import log_fun

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 取给定路径上一级的路径
sys.path.append(BASE_DIR)
# 添加环境变量
pwd_path = os.path.join(BASE_DIR, 'user.pkl')
try:
    with open(pwd_path,'rb') as file:
        pwd = pickle.load(file)  # 传入密码文件
except Exception as e:
    print(' ')
    pwd = {}
logger = log_fun.fudamai_log()

class Memo:
    def __init__(self,name, thing, date):
        self._id = 1
        self.name = name
        self.thing = thing
        self.date = date


    @property
    def id(self):
        "定义内部变量id的可视"
        return self._id


    @id.setter
    def id(self,num_len):
        "定义id的可更改。测试不加setter属性，结果：类属性被覆盖，每个类的id返回值都一样"
        self._id = num_len
    

    def __str__(self):
        # __str__方法必须设置返回值
        return f'事件：{self.id}\n名称：{self.name }\n内容：{self.thing}\n发生时间：{self.date}'


class MemoAdmin:

    def __init__(self,user,password):
        self.user = user
        self.password = password
        pass
        

    def add(self):
        "添加记录，并把记录保存到memo_list中"
        "用户输入参数，并根据输入生成类"
        self.load()  # 载入文件
        try:            
            in_name = input('名称：')
            in_thing = input('内容：')                
            in_date = input('发生时间：')
            print('待办列表'.center(30, '-')) 
           
            # 直接使用类对象,不实例类对象也可
            count = len(self.memo_list)
            memo = Memo(in_name, in_thing, in_date)
            self.memo_list.append(memo)
            if count == 0:
                pass
            elif count >= 1: 
                memo.id = self.memo_list[-2].id + 1  # 最后一个id加1就是新的id
        except Exception as e:
            print('添加memo出错啦！', e)   
            logger.warning('添加memo出错')     
        self.save()  # 保存文件
        logger.info('保存一条备忘')

    def delete(self):
        "删除以保存的记录,根据索引删除"
        # 删除前需查看
        try:
            memo_class_d = self.query()
            self.memo_list.remove(memo_class_d)
            print('此ID备忘已删除')
        except Exception as e:
            print(e)
        self.save()
        logger.info('删除一条备忘')

    def modify(self):
        "修改已保存的记录"
        # 修改类属性
        memo_class_m = self.query()
        memo_class_m.name = input('新的的名称：')
        memo_class_m.thing = input('新的内容：') 
        memo_class_m.date = input('新的发生时间：')
        self.save()
        logger.info('修改一条备忘')

    def query(self):
        "输入ID查询记录"
        # 查询前需导入文件
        self.load()
        print(f'共{len(self.memo_list)}条备忘')
        try:        
            id_num = int(input('请输入记录的ID：'))
            a = 0
            for each in self.memo_list:
                if id_num == each.id:
                    print(each)                            
                    return each
                else:
                    a = 1
            if a == 1:
                print('ID不存在。')
        except Exception as TE:
            print('请输入纯数字！', TE)
        logger.info('查询备忘一次')
        

    def save(self):
        "将输入的记录进行保存成文件,保存文件在退出时进行"
        "调用配置中的da_path，并将其指定为文件保存路径"
        # cof_path = os.path.join(BASE_DIR, f'{self.user}.pkl')
        # with open(cof_path, 'rb') as cof:
        #     data = pickle.load(cof)  # 加载的文件就是configparser对象
        #     da_path = data[self.user]['da_path']
        da_path = self.load_config()
        with open(da_path, 'wb') as f:
            f.write(pickle.dumps(self.memo_list))
        print('备忘已保存')
        logger.info('备忘已保存')

    def load(self):
        "将保存的文件反序列化，以方便查询"
        "根据用户名从配置文件中找到备忘保存地址，并打开"
        da_path = self.load_config()
        try:
            with open(da_path, 'rb') as f:
                self.memo_list = pickle.load(f)
        except Exception as e:
            print('没有已保存备忘', e)
            self.memo_list = []
        
        return self.memo_list 
        logger.info('载入备忘数据一次')
    

    def to_pdf(self):
        "将历史备忘输出为PDF"
        self.load()  
        try:
            for each in self.memo_list:
                pdf = pdf_demo.ExportPDF(each.text())
                pdf.save_text()
        except Exception as e:
            print('输出失败', e)        
            logger.error('输出PDF失败')    
        logger.info('将历史备忘输出为PDF')
        

    def quit(self):
        logger.info('离开备忘操作界面')
        return 'quit'
        
      
    def login(self):
        "输入用户名，密码。判断是否匹配"
        # user = input('请输入用户名：')
        # password = input('请输入密码：')        
        print('启动登录验证。')

        if self.user in pwd :  # 判断用户名存在与否
            self.load_config()
            if self.password == pwd[self.user]:  # 判断密码是否匹配
                self.choose()
            else:
                print('密码不正确。')
        else:
            print('用户名不存在。')
            turn = input('是否创建新用户（y|n）：')
            if turn == 'y':
                self.register()   
            elif turn == 'n':
                return 'again'
            else:
                print('请按指示输入')
                return 'again'
        logger.info('用户登录')
                
    def load_config(self):
        "载入配置文件"
        # user = input('请输入用户名：')
        cof_path = os.path.join(BASE_DIR, f'{self.user}.pkl')
        with open(cof_path, 'rb') as cof:
            data = pickle.load(cof)  # 加载的文件就是configparser对象
            # print(data)
            # print(data.sections())
            print(data[self.user]['da_path'])

        if self.user in data.sections():
            print('ok')              
            return data[self.user]['da_path']  
            logger.info('载入用户配置一次')
        else:
            print('未找到用户的配置')
            logger.warning('未找到用户的配置')

    
    def register(self):
        "用户注册，并保存配置"
        # 用户名及密码区分大小写
        user = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        pwd[user] = password
        pwd_path = os.path.join(BASE_DIR, 'user.pkl')
        with open(pwd_path, 'ab') as f:
            f.write(pickle.dumps(pwd))  # 保存用户密码

        da_path = os.path.join(BASE_DIR, F'{user}.db')
        config = configparser.ConfigParser()
        config.add_section(user)
        config.set(user, 'da_type', 'db')
        config.set(user, 'da_path', da_path)
        config.set(user, 'da_name', user + '.db')

        cog_path = os.path.join(BASE_DIR, f'{user}.pkl')
        with open(cog_path, 'ab') as da_f:
            da_f.write(pickle.dumps(config))  # 保存用户配置
        logger.warning('一名用户注册')
    
    
    def choose(self):
        "根据用户输入选择不同的功能"
        print('想进行哪些操作？')
        menu = {
            '命令':'对应功能',
            'add':'即添加一条新的备忘',
            'delete':'删除过往保存的某条备忘',
            'modify':'修改过往保存的某条备忘',
            'query':'查看过往保存的备忘。根据事件名或ID查看详细内容。',
            'pdf':'将历史备忘输出为PDF',
            'quit':'退出程序'
        }
        for k,v in menu.items():
            print(k,v)
             
        while True:  
            choose = input('请输入要执行的功能：').strip().lower()     
            if choose == 'add':
                self.add()
                logger.info('用户进行一次添加操作')
            elif choose == 'delete':
                self.delete()
            elif choose == 'modify':
                self.modify()
            elif choose == 'query':
                self.query()
            elif choose == 'pdf':
                self.to_pdf()
            elif choose == 'quit':
                self.quit()
                break
            else:
                print('待开发功能')
            

def main():
    menu = {
        '1':'启动备忘程序',
        '2':'退出程序'
    }
    for k,v in menu.items():
        print(f'{k}:{v}')
    turn = input('启动或退出程序（y|n）：').strip().lower()
    while True:
        if turn == 'y':
            print('程序启动。输入用户名、密码进行登录。')
            user = input('请输入用户名：').strip()
            password = input('请输入密码：').strip()
            admin = MemoAdmin(user,password)
            admin.login()
        elif turn == 'n':
            print('即将退出程序。')
            break
        else:
            print('请输入 y 或 n。')
        turn = input('启动或退出程序（y|n）：').strip().lower()


if __name__ == '__main__':
    main()