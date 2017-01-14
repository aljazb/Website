from .models import Topic, Comment
from django.shortcuts import render, redirect
from .forms import CommentPostForm, TopicPostForm
from devices.models import Device
from django.http import HttpResponseForbidden, Http404
import logging
import re

logger = logging.getLogger(__name__)


def topic(request, topic_id):
    """Returns the rendered page that shows the topic and the belonging comments

    the method checks whether the request is GET (the user requested to see a topic) and POST (the user posted a comment)
    The POST method checks if the user is logged in and in that case saves the comment to the database

    Keyword arguments:
    request -- HttpRequest object
    topic_id -- the id of a topic to be displayed
    """
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
        comment_pattern = re.compile('^[.,a-zA-Z ]+$')
        body = request.POST['body']

        if user is not None and comment_pattern.match(body):
            comment = form.save(commit=False)
            comment.topic = curr_topic
            comment.author = user
            comment.body = body
            comment.hearts = 0
            comment.save()
            return redirect('/forum/' + topic_id)

        return render(request, template_name, context)


def topic_heart(request, topic_id):
    """Increments the heart count on a given topic

    Can only be accessed by a logged in user

    Keyword arguments:
    request -- HttpRequest object
    topic_id -- the id of a topic
    """
    liked_topic = Topic.objects.get(id=topic_id)
    liked_topic.hearts += 1
    liked_topic.save()
    return redirect('/forum/' + topic_id)


def comment_heart(request, comment_id):
    """Increments the heart count on a given comment

    Can only be accessed by a logged in user

    Keyword arguments:
    request -- HttpRequest object
    comment_id -- the id of a comment
    """
    liked_comment = Comment.objects.get(id=comment_id)
    liked_comment.hearts += 1
    liked_comment.save()
    return redirect('/forum/' + str(liked_comment.topic.id))


def new_topic(request, device_id):
    """Returns the rendered page that is used for writing new topics

    The method checks whether the request is GET (the user requested a page used to write a new topic) and POST (the user posted a new topic)
    The POST method checks if the user is logged in and in that case saves the topic to the database and redirects to that page


    Keyword arguments:
    request -- HttpRequest object
    device_id -- the id of a device for redirect purposes
    """
    form_class = TopicPostForm
    template_name = 'forum/new_topic.html'

    if request.method == 'GET':
        return render(request, template_name, {})
    elif request.method == 'POST':
        user = request.user
        form = form_class(request.POST)
        topic_pattern = re.compile('^[.,a-zA-Z ]+$')
        body = request.POST['body']

        if user is not None and topic_pattern.match(body):
            new_topic_device = form.save(commit=False)
            new_topic_device.device = Device.objects.get(id=device_id)
            new_topic_device.author = user
            new_topic_device.body = body
            new_topic_device.hearts = 0
            new_topic_device.save()
            return redirect('/forum/' + str(new_topic_device.id))

        return render(request, template_name, {})


def delete_comment(request, comment_id):
    """Deletes the specified comment

    Check if a user is logged in and if he is the one who posted the comment or if he has the delete permissions
    In that case the comment is deleted from the database. Otherwise a 403 is returned telling the user he doesn't have permission

    Keyword arguments:
    request -- HttpRequest object
    comment_id -- the id of a comment
    """
    deleted_comment = Comment.objects.get(id=comment_id)
    if request.user.has_perm('forum.delete_comment') or request.user == deleted_comment.author:
        deleted_comment = Comment.objects.get(id=comment_id)
        current_topic = deleted_comment.topic
        logger.debug('[Comment deleted] user: ' + request.user.username + '; comment: ' + deleted_comment.body + '; topic: ' + current_topic.body)
        deleted_comment.delete()
        return redirect('/forum/' + str(current_topic.id))
    return HttpResponseForbidden("You do not have permission to delete this comment.")


def delete_topic(request, topic_id):
    """Deletes the specified comment

    Check if a user is logged in and if he is the one who posted the topic or if he has the delete permissions
    In that case the topic is deleted from the database. Otherwise a 403 is returned telling the user he doesn't have permission

    Keyword arguments:
    request -- HttpRequest object
    topic_id -- the id of a comment
    """
    deleted_topic = Topic.objects.get(id=topic_id)
    if request.user.has_perm('forum.delete_comment') or request.user == deleted_topic.author:
        current_device = deleted_topic.device
        logger.debug('[Topic deleted] user: ' + request.user.username + '; topic: ' + deleted_topic.body)
        deleted_topic.delete()
        if current_device is None:
            return redirect('/home')
        return redirect('/devices/' + str(current_device.id))
    return HttpResponseForbidden("You do not have permission to delete this post.")
