from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from markdown import markdown

# Create your models here.
class Topic(models.Model):
    # TODO:修改为BBS 样式的类名
    # author = models.CharField(max_length=50, default='fubai')
    author = models.ForeignKey(User, default=1 , on_delete=models.CASCADE, verbose_name='作者')
    topic_text = models.CharField('帖子标题', max_length=2000)
    topic_description = models.TextField('帖子正文', max_length=2000)
    pub_date = models.DateTimeField('日期', auto_now_add=True)
    picture = models.FileField(blank=True, null=True)

    def get_topic_text_md(self):
        return mark_safe(markdown(self.topic_description))

    def __str__(self):
        return self.topic_text

    class Meta:
        verbose_name = '帖子'
        verbose_name_plural = '帖子'


class Reply(models.Model):
    # author = models.CharField(max_length=50, default='fubai')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='帖子')
    reply_text = models.TextField('跟帖', max_length=2000)
    author = models.ForeignKey(User, default=1 , on_delete=models.CASCADE, verbose_name='作者')
    # 添加图片字段。可以为空，默认为空。
    picture = models.FileField(blank=True, null=True)
    pub_date = models.DateTimeField('日期', auto_now_add=True)

    def get_reply_text_md(self):
        return mark_safe(markdown(self.reply_text))

    def __str__(self):
        return self.reply_text

    class Meta:
        verbose_name = '跟帖'
        verbose_name_plural = '跟帖'