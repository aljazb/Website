from __future__ import unicode_literals

from django.db import models
from devices.models import Device
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone


class Topic(models.Model):
    """Class representing the Topic object

    This class represents a topic, which can be associated with a device or standalone
    The latter is displayed on the home page
    """
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, blank=True, null=True, default=None)
    body = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hearts = models.IntegerField(default=0)

    def __str__(self):
        """String representation of Topic"""
        return self.body

    def is_recent(self):
        """Returns True if a Topic was posted less than 3 days before, otherwise it returns False"""
        return self.date + timedelta(days=3) >= timezone.now()


class Comment(models.Model):
    """Class representing the Topic object

    This class represents a comment, which has be associated with a topic
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    body = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hearts = models.IntegerField(default=0)

    def __str__(self):
        """String representation of Comment"""
        return self.body
