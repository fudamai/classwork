from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    IMPORTANT_CHOICE = (
        ('1', '不重要不紧急'),
        ('2', '重要不紧急'),
        ('3', '不重要但紧急'),
        ('4', '重要且紧急'),
    )
    CLASS_DICT = {
        IMPORTANT_CHOICE[0][0]: 'success',
        IMPORTANT_CHOICE[1][0]: 'warning',
        IMPORTANT_CHOICE[2][0]: 'info',
        IMPORTANT_CHOICE[3][0]: 'danger',
    }
    FINISH_STATUS = (
    ('doing', '进行中'),
    ('done', '已完成'),
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    duedate = models.DateField(default=timezone.now)
    important = models.CharField(choices=IMPORTANT_CHOICE, max_length=10, default='4')
    finish = models.CharField(max_length=10, choices=FINISH_STATUS, default="doing")
    class_type = models.CharField(max_length=50, default='success')
    author = models.ForeignKey(User, default=2, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_class_type(self):
        return self.CLASS_DICT[self.important]