import configparser
import pickle
import os


"""添加配置文件，保存信息：
自动登录配置、用户名及密码、密钥
以IP为section，username为option，密码为value
一个IP下可以保存多个用户。
"""

# 可以用用户名或者IP地址作为session，

# config['root'] = {
#     'host':'192.168.87.129',
#     'username':'root',
#     'password':'wodeps4'
# }

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Config():
    """保存用户名、IP地址、密码
    """
    def __init__(self, ip):
        self.config = configparser.ConfigParser()
        self.ip = ip

    def add_section(self, user, password):
        """添加以ip地址为section的配置文件
        """
        self.config.add_section(self.ip)
        self.config.set(self.ip, user, password)
        print(password)
        # self.config.set(self.ip, 'password', password)

        cog_path = os.path.join(BASE_DIR, f'{self.ip}.pkl')
        with open(cog_path, 'wb') as da_f:  # w模式。覆盖旧的文件
            da_f.write(pickle.dumps(self.config))
            print('添加配置成功')


    def load_config(self):
        """输出用户名，ip地址，密码
        """
        cog_path = os.path.join(BASE_DIR, f'{self.ip}.pkl')
        with open(cog_path, 'rb') as file:
            con_db = pickle.load(file)
        print(f"用户{self.ip}配置的用户有{con_db.options(self.ip)}")

        if self.ip in con_db.sections():
            print('ok')
            # print(con_db.options(self.ip))
            # print(con_db.sections())
            # print(con_db[self.ip][con_db.options(self.ip)[0]])
            return self.ip, con_db.options(self.ip)[0], con_db[self.ip][con_db.options(self.ip)[0]]  # 注意输出的是列表
        else:
            print('未找到此用户的配置文件')
        

def main():
    admin = Config('192.168.235.132')
    # admin.add_section('root', 'wodeps4')
    admin.load_config()

# 未完成项：写入配置文件，载入配置文件
if __name__ == '__main__':
    main()