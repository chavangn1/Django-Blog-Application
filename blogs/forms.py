from django import forms
from .models import BlogPostsModel, CommentsModel

class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = BlogPostsModel
        exclude = '__all__'


class CreateComment(forms.ModelForm):
    class Meta:
        model = CommentsModel
        exclude = '__all__'