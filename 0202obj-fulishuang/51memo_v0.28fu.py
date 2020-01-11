#! python
# -*- coding:utf-8 -*-
# Author:fudamai
# 51memo_v0.27


"""
备忘录程序
问题：由于ID是由memo_list生成。当删除一个备忘后，新添加的备忘ID与上一个备忘相同
self.query()的参数id_num,实际上是memo_list的索引值。删除一个备忘后，也会导致id_num与self._id不一致。
解决方法：去除delete方法，通过修改已保存备忘来清除不想要的备忘。这里不做更改
"""

import pickle


class Memo:
    def __init__(self,name, thing, date):
        self._id = 0
        self.name = name
        self.thing = thing
        self.date = date


    @property
    def id(self):
        "定义内部变量id的可视"
        return self._id


    @id.setter
    def id(self, num_len):
        "定义ID的可更改"
        self._id = num_len


    def __str__(self):
        # __str__方法必须设置返回值
        return f'事件：{self.id}\n名称：{self.name }\n内容：{self.thing}\n发生时间：{self.date}'


class MemoAdmin:

    def __inti__(self):
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
            # 使用实例对象
            # memo = Memo(in_name, in_thing, in_date)               
            # # memo._id = len(self.memo_list) + 1  # 直接使用下换线修改内部变量，不用定义Memo类@id.setter属性
            # memo.id = len(self.memo_list) + 1
            # self.memo_list.append(memo)
            # 直接使用类对象,不实例类对象也可
            self.memo_list.append(Memo(in_name, in_thing, in_date))
            Memo.id = len(self.memo_list)
        except Exception as e:
            print('添加memo出错啦！', e)        
        self.save()  # 保存文件


    def delete(self):
        "删除以保存的记录,根据索引删除"
        # 删除前需查看
        memo_class_d = self.query()
        self.memo_list.remove(memo_class_d)
        print('此ID备忘已删除')
        self.save()


    def modify(self):
        "修改已保存的记录"
        # 修改类属性
        memo_class_m = self.query()
        # print(memo_class_m)  # 运行这一句会出现两条记录
        memo_class_m.name = input('新的的名称：')
        memo_class_m.thing = input('新的内容：') 
        memo_class_m.date = input('新的发生时间：')
        self.save()


    def query(self):
        "输入ID查询记录"
        # 查询前需导入文件
        self.load()
        print(f'共{len(self.memo_list)}条备忘')
        try:        
            id_num = int(input('请输入记录的ID：'))
            print(self.memo_list[id_num - 1])            
            return self.memo_list[id_num - 1]
        except IndexError as IE:
            print('此ID不存在！', IE)  
        except TypeError as TE:
            print('请输入纯数字！', TE)
        # for i in self.memo_list:
        #     print(i)


    def save(self):
        "将输入的记录进行保存成文件,保存文件在退出时进行"
        with open('db.pkl', 'wb') as f:
            f.write(pickle.dumps(self.memo_list))
        print("备忘已保存")

    
    def load(self):
        "将保存的文件反序列化，以方便查询"
        try:
            with open('db.pkl', 'rb') as file:
                self.memo_list =pickle.load(file)
        except Exception as error:
            print('没有已保存记录', error)
            self.memo_list = []
        return self.memo_list   
        

    def quit(self):
        return 'quit'


def main():
    "程序主入口"
    admin = MemoAdmin()
    print('想进行哪些操作？')
    menu = {
        '命令':'对应功能',
        'add':'即添加一条新的备忘',
        'delete':'删除过往保存的某条备忘',
        'modify':'修改过往保存的某条备忘',
        'query':'查看过往保存的备忘。根据事件名或ID查看详细内容。',
        'quit':'退出程序'
    }
    # print(menu)  # 示意
    for k,v in menu.items():
        print(k,v)
  
    turn = True
    while turn:  
        choose = input('请输入要执行的功能：').strip()
        func = getattr(admin, choose)  # 用户可以输入键或值，判断输入是否存在。调用方法，并赋值给变量
        if(func):            
            if func() == 'quit':
                break
        else:
            print('没有这个操作')
        
        
if __name__ == '__main__':
    main() 