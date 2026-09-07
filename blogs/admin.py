from django.contrib import admin
from .models import BlogPostsModel, CommentsModel
# Register your models here.

admin.site.register(BlogPostsModel)
admin.site.register(CommentsModel)