from django import forms
from .models import BlogPostsModel, CommentsModel


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = BlogPostsModel
        fields = ['title', 'description', 'category', 'photo']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'text-sm border border-gray-400 w-full p-2 rounded-md'
            }),
            'description': forms.Textarea(attrs={
                'class': 'text-sm border border-gray-400 w-full p-2 rounded-md h-20'
            }),
            'category': forms.Select(attrs={
                'class': 'text-sm border border-gray-400 w-full p-2 rounded-md'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'text-sm border border-gray-400 w-full p-2 rounded-md'
            }),
        }


class CreateCommentForm(forms.ModelForm):

    class Meta:
        model = CommentsModel
        fields = ['comment']

        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'w-full h-20 border border-gray-300 rounded-lg p-3',
                'rows': 4,
                'placeholder': 'Write your comment...'
            })
        }


class EditCommentForm(forms.ModelForm):

    class Meta:
        model = CommentsModel
        fields = ['comment']

        labels = {
            'comment': 'Edit Comment'
        }

        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-3',
                'rows': 4,
                'placeholder': 'Edit your comment...'
            })
        }
