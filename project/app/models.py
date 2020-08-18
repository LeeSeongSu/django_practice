from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class Article(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/',blank=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="writer", default="")


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username
    nickname = models.CharField(max_length=20,default = '')
    phone_number = models.CharField(max_length=20,default = '')    
    grade = models.CharField(max_length=20,default = '')
    major = models.CharField(max_length=20,default = '')

class Comment(models.Model):
    def __str__(self):
        return self.text

    c_writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="c_writer", default="")
    post_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=50)