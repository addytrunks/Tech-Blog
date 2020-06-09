from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = RichTextField(blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    # text = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=30,default='coding')
    likes = models.ManyToManyField(User,related_name='blog_like')

    def get_absolute_url(self):
        return reverse('blog:home')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

class Category(models.Model):
    name = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('blog:home')

    def __str__(self):
        return self.name
