from django.db import models
from django.utils import timezone

from admin_app.models import Category
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    text = models.TextField()
    image = models.ImageField(upload_to='post/covers', default='post/covers/default.png')
    num_comments = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
