from __future__ import unicode_literals

from django.db import models
from devices.models import Device
from django.contrib.auth.models import User
from datetime import datetime


class Topic(models.Model):
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True)
    body = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hearts = models.IntegerField()


class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    body = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hearts = models.IntegerField()
