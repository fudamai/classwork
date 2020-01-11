#! python
# -*- coding:utf-8 -*-
# Author:fudamai
# ImageUtil.py


"""
图像处理类，选取目录中所有图片类型文件（jpg、png、bmp),并用Excel存档：第一列为文件名，第二列为文件大小
可根据命令行参数，对图像进行旋转，裁剪操作
整个工程包含多个目录，包含配置文件、日志记录、数据文件
"""

import sys
import openpyxl
import os
import re
from PIL import Image
from PIL import ImageDraw, ImageFont
import log_fun
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
target_dir = os.path.join(BASE_DIR, 'target_dir')
source_dir = os.path.join(BASE_DIR, 'kuqi')


class ImageSystem:
    
    """照片管理系统"""
    def __init__(self,im_name, source_dir=source_dir, target_dir=target_dir):
        self.im_name = im_name
        self.file_path = os.path.join(source_dir, im_name)
        self.source_dir = source_dir
        self.target_dir = target_dir
        self.logger = log_fun.fudamai_log(logger_name='ImageSystem')
        
    def thumbnail(self, percent=0.5):
        """生成缩略图
        默认缩放比例0.5"""
        # 打开一个JPG图像文件。注意路径
        im = Image.open(self.file_path)
        print(im.format, im.size, im.mode)

        w, h = im.size
        print('尺寸：%s*%s' % (w, h)) 

        im.thumbnail((int(w*percent), int(h*percent)), resample=4)  # 生成缩略图
        print('Resize image to:%s*%s' % (int(w*percent), int(h*percent)))
        try:
            new_name, target_name = self.autoname(self.im_name, 'thumbnail')
            im.save(target_name)
            self.logger.info('生成缩略图')
        except Exception as e:
            self.logger.warning(e)
    
    def autoname(self, name, pre):
        """自动命名,传入文件名及处理方法
        ,将处理方法作为后缀加入文件名
        """
        re_name = re.compile('\.\w{0,4}?$')
        match = re_name.search(name)
        try:
            new_name = re_name.sub(f'-{pre}{match.group()}', name)
            self.logger.info('重命名')
            target_name = os.path.join(self.target_dir, new_name)
            return new_name, target_name
        except Exception as e:
            self.logger.error(f'{e}文件后缀名不匹配')
            print('文件后缀名不匹配')

    def thumbnail_ll(self, percent=0.5):
        """生成给定路径source_dir下所有的缩略图"""
        self.thumbnail()

    def resize(self, h_ratio, w_ratio):
        """调整大小
        按比例调整，h-tatio高的比例，w_ratio宽的比例
        """        
        pass

    def rotate(self, angle, isMirror):
        """旋转，包含镜像
        angle:角度。
        isMirror的参数：水平翻转：{acl:aclinic}、垂直翻转：{ver:vertical}
        """

        try:
            new_name, target_name = self.autoname(self.im_name, '-rotate')
            # target_name = os.path.join(self.target_dir, new_name)
            # file_path = os.path.join(self.source_dir, self.im_name)
            im = Image.open(self.file_path)
            if type(angle) == int:
                print(angle)
                r_im = im.rotate(angle,expand=True)  # 设置补全像素参数
                if self.mirror(isMirror, r_im) == None:
                    r_im.save(target_name)
                    self.logger.info('只旋转图像，不翻转')
                else:
                    m_im = self.mirror(isMirror, r_im)
                    m_im.save(target_name)
                    self.logger.info('旋转图像，同时翻转')
            else:
                self.logger.warning('angle参数错误')
                print('angle参数错误')
        except Exception as e:
            self.logger.error(e)


    def mirror(self, axes, r_im):
        """根据输入参数进行不同的镜像翻转
        此方法第二个参数为Image类，在rotate中调用"""
        if axes == 'n':
            self.logger.info('使用默认翻转参数')
            return None            
        elif axes == 'acl':
            m_im = r_im.transpose(Image.FLIP_LEFT_RIGHT)
            self.logger.info('左右翻转')
            return m_im
        elif axes == 'ver':
            m_im = r_im.transpose(Image.FLIP_TOP_BOTTOM)
            self.logger.info('上下翻转')
            return m_im
        else:
            print('isMirror参数不正确。')
            self.logger.warning('参数不正确')
            return None

    def region(self):
        """根据输入的坐标裁剪图像
        输入坐标顺序：左右上下
        """
        print('使用裁剪功能')
        new_name, target_name = self.autoname(self.im_name, '-region')
        try:
            box = input('请输入四元组坐标：').split(sep=',')
            box_int = (int(x) for x in box)
            im = Image.open(self.file_path)
            cut_im = im.crop(box_int)
            cut_im.save(target_name)
            self.logger.info('裁剪图片并保存')
        except Exception as e:
            self.logger.warning('裁剪坐标错误')
            print('请输入正确坐标')

    def add_logo(self):
        """添加logo"""
        pass
    
    def new_image(self, words, position, font, color):
        """新建一个图，并添加文字"""
        pass


    def name_to_excel(self):
        """将目录文件夹中图片名整理保存至Excel"""
        wb = openpyxl.Workbook()
        sh1 = wb.active
        sh1['A1'] = '文件名'
        sh1['B1'] = '像素尺寸'
        index = 2
        format_list = ['.jpg', '.bmp', '.png']
        try:
            # or_dir = input('输入文件夹路径：')
            # print(or_dir)
            for root, dirs, files in os.walk(self.file_path):
                for name in files:
                    # print(name)
                    if name[-4:] in format_list:
                        im = Image.open(os.path.join(self.source_dir, name))
                        # im.size
                        sh1['A' + str(index)] = name
                        sh1['B' + str(index)] = ('%s*%s' % im.size)                    
                        index += 1
        except Exception as e:
            self.logger.warning(f'{e}路径错误')
        target_name = os.path.join(self.target_dir, 'image_name_all.xlsx')
        wb.save(target_name)
        self.logger.info('整理指定文件夹中的图片名并保存至Excel')
     

    def help(self):
        "输出支持的命令行参数列表"
        print("""
        usage:
        -rg or --region,裁剪图像
        -rt or --rotate,旋转图像
        """
        )

def main():
    menu = {
            'th':'生成缩略图',        
            'rt':'旋转图像，可以镜像翻转',        
            'rg':'根据输入的坐标裁剪图像',
            'nte':'将目录文件夹中图片名整理保存至Excel',
            'quit':'退出程序'
        }
    print(f'请将需处理的图片放入一下路径{source_dir}')
    im_name = input('请输入目标路径名：')
    image = ImageSystem(im_name)
    for k, v in menu.items():
        print(k, v)
    
    count = len(sys.argv)

    while count==1:
        choose = input('请输入要执行的功能：').strip().lower()     
        if choose == 'tb':
            image.thumbnail()
            image.logger.info('调用thumbnail方法')
        elif choose == 'rt':
            angle = input('请输入旋转角度：')
            mirror = input('输入镜像规则（n键跳过）')
            image.rotate(int(angle), mirror)
            image.logger.info('调用rotate方法')
        elif choose == 'rg':
            image.region()
            image.logger.info('调用region方法')
        elif choose == 'nte':
            image.name_to_excel()
            image.logger.info('调用name_to_excel方法')
        elif choose == 'quit':
            image.logger.info('调用quit方法')
            print('即将退出')
            break
        else:
            print('待开发功能')           
            image.logger.warning('未指定功能代码')
    if sys.argv[1] in {'-rg', '--region'}:
        image.region()
        image.logger.debug('调用region方法')
    elif sys.argv[1] in {'-rt', '--rotate'}:
        angle = input('请输入旋转角度：')
        mirror = input('输入镜像规则（n键跳过）')
        image.rotate(int(angle), mirror)
        image.logger.debug('调用rotate方法')
    elif sys.argv[1] in {'-h', '--help'}:
        image.help()
        image.logger.debug('调用help方法，查看帮助')
    else:
        image.logger.debug('未定义的命令行参数')

if __name__ == '__main__':
    main()


        
