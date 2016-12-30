from django.shortcuts import render
from .models import Topic, Comment
from django.shortcuts import render, redirect


def topic(request, topic_id):
    context = {
        "topic": Topic.objects.get(id=topic_id),
        "comments": Topic.objects.get(id=topic_id).comment_set.all(),
    }

    return render(request, 'forum/forum.html', context)


def topic_heart(request, topic_id):
    liked_topic = Topic.objects.get(id=topic_id)
    liked_topic.hearts += 1
    liked_topic.save()
    return redirect('/forum/' + topic_id)


def comment_heart(request, comment_id):
    liked_comment = Comment.objects.get(id=comment_id)
    liked_comment.hearts += 1
    liked_comment.save()
    return redirect('/forum/' + str(liked_comment.topic.id))