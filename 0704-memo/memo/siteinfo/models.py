from django.db import models

# Create your models here.
class Banner(models.Model):
    # 展示区数据模型
    title = models.CharField(max_length=50, default='HELLO WORLD!')
    
    def __str__(self):
        return self.title


class Item(models.Model):
    # 脚部信息列中的一个信息
    title = models.CharField(max_length=20)
    url = models.URLField()
    col = models.ForeignKey('Col', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Col(models.Model):
    # 脚部信息的一个列
    title = models.CharField(max_length=50, default='col1')
    footer = models.ForeignKey('Footer', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    

class Footer(models.Model):
    # 脚部数据模型
    title = models.CharField(max_length=50, default='footer1')
    
    def __str__(self):
        return self.title