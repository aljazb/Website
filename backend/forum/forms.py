from django import forms
from .models import Topic, Comment


class TopicPostForm(forms.ModelForm):
    """Form used for writing a new topic"""
    class Meta:
        model = Topic
        fields = ['body']


class CommentPostForm(forms.ModelForm):
    """Form used for writing a new comment"""
    class Meta:
        model = Comment
        fields = ['body']