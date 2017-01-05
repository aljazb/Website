from .models import Topic, Comment
from django.shortcuts import render, redirect
from .forms import CommentPostForm, TopicPostForm
from devices.models import Device
from django.http import HttpResponseForbidden, Http404
import logging

logger = logging.getLogger(__name__)


def topic(request, topic_id):
    form_class = CommentPostForm
    template_name = 'forum/forum.html'
    curr_topic = Topic.objects.get(id=topic_id)

    context = {
        "topic": curr_topic,
        "comments": Topic.objects.get(id=topic_id).comment_set.all(),
    }

    if request.method == 'GET':
        return render(request, template_name, context)
    elif request.method == 'POST':
        user = request.user
        form = form_class(request.POST)

        if user is not None:
            comment = form.save(commit=False)
            comment.topic = curr_topic
            comment.author = user
            comment.body = request.POST['body']
            comment.hearts = 0
            comment.save()
            return redirect('/forum/' + topic_id)

        return render(request, template_name, context)


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


def new_topic(request, device_id):
    form_class = TopicPostForm
    template_name = 'forum/new_topic.html'

    if request.method == 'GET':
        return render(request, template_name, {})
    elif request.method == 'POST':
        user = request.user
        form = form_class(request.POST)

        if user is not None:
            new_topic_device = form.save(commit=False)
            new_topic_device.device = Device.objects.get(id=device_id)
            new_topic_device.author = user
            new_topic_device.body = request.POST['body']
            new_topic_device.hearts = 0
            new_topic_device.save()
            return redirect('/forum/' + str(new_topic_device.id))

        return render(request, template_name, {})


def delete_comment(request, comment_id):
    deleted_comment = Comment.objects.get(id=comment_id)
    if request.user.has_perm('forum.delete_comment') or request.user == deleted_comment.author:
        deleted_comment = Comment.objects.get(id=comment_id)
        current_topic = deleted_comment.topic
        logger.debug('[Comment deleted] user: ' + request.user.username + '; comment: ' + deleted_comment.body + '; topic: ' + current_topic.body)
        deleted_comment.delete()
        return redirect('/forum/' + str(current_topic.id))
    return HttpResponseForbidden("You do not have permission to delete this comment.")


def delete_topic(request, topic_id):
    deleted_topic = Topic.objects.get(id=topic_id)
    if request.user.has_perm('forum.delete_comment') or request.user == deleted_topic.author:
        current_device = deleted_topic.device
        logger.debug('[Topic deleted] user: ' + request.user.username + '; topic: ' + deleted_topic.body + '; device: ' + current_device.name)
        deleted_topic.delete()
        if current_device is None:
            return redirect('/home')
        return redirect('/devices/' + str(current_device.id))
    return HttpResponseForbidden("You do not have permission to delete this post.")
