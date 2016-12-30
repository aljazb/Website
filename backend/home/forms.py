from django import forms
from forum.models import Topic


class TopicPostForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['body']