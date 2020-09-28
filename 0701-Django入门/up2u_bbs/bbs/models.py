from django.db import models

# Create your models here.
class Topic(models.Model):
    # TODO:修改为BBS 样式的类名
    author = models.CharField(max_length=50, default='fubai')
    topic_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic_text


class Reply(models.Model):
    author = models.CharField(max_length=50, default='fubai')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    reply_text = models.CharField(max_length=200)

    def __str__(self):
        return self.reply_text