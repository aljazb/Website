from django import forms
from .models import Topic, Comment


class TopicPostForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['body']


class CommentPostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']