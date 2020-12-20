from django.db import models

# Create your models here.
class Zones(models.Model):
    zone = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.zone


class Comments(models.Model):
    owner = models.ForeignKey('auth.User', related_name='user_comment', on_delete=models.CASCADE)
    blog = models.ForeignKey('Blogs', related_name='blog_comment', on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='blogs', on_delete=models.CASCADE)
    # tags = models.ManyToManyField(Tags)
    tags = models.CharField(max_length=100, blank=True, default="")
    imgUrl = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)