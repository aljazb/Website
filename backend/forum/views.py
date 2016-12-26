from django.shortcuts import render
from .models import Topic, Comment


def topic(request, topic_id):
    context = {
        "topic": Topic.objects.get(id=topic_id),
        "comments": Topic.objects.get(id=topic_id).comment_set.all(),
    }
    return render(request, 'forum/forum.html', context)
