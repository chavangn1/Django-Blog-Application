from django.db import models
from accounts.models import User
# Create your models here.

class BlogPostsModel(models.Model):
    categories = (
            ('science and tech','science and tech'),
            ('politics', 'politics'),
            ('sports', 'sports'),
            ('infrasture', 'infrasture'),
            ('finance', 'finance')
        )
    tiltle = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(choices=categories, max_length=40)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='blog_photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tiltle

class CommentsModel(models.Model):
    comment = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPostsModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
