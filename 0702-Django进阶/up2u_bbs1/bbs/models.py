from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    # TODO:修改为BBS 样式的类名
    # author = models.CharField(max_length=50, default='fubai')
    author = models.ForeignKey(User, default=1 , on_delete=models.CASCADE)
    topic_text = models.CharField(max_length=200)
    topic_description = models.CharField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True)
    picture = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.topic_text


class Reply(models.Model):
    # author = models.CharField(max_length=50, default='fubai')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    reply_text = models.CharField(max_length=200)
    author = models.ForeignKey(User, default=1 , on_delete=models.CASCADE)
    # 添加图片字段。可以为空，默认为空。
    picture = models.FileField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.reply_text