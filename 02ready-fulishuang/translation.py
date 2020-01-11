print('欢迎使用汉译英词典'.center(30,'-'))
orig_dict = {'中文': 'chinese',
 '书': 'book',
 '代码': 'code',
 '字典': 'dictionary',
 '英语': 'English',
 '生活': 'life'}
for k, v in orig_dict.items():
    print(k, v)
    
query = input('请输入要查询的中文：')

# 判断是否存在
exist = orig_dict.get(query, '1')
if exist == '1':
    print("没有找到对应翻译，是否添加新的翻译条目", end = ' ')
    choice = input("添加翻译Y,不添加N:").casefold()
    if choice == 'y':
        cn = input("请输入中文：")
        en = input("请输入对应的英语翻译：")
        orig_dict[cn] = en
        print("添加成功")
    elif choice == 'n':
        print("再见")
else:
    print(f'{query}的英文翻译是：{orig_dict[query]}') 