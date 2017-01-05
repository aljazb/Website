from django.test import TestCase
from .models import Topic, Comment
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class ArticleTests(TestCase):

    def setUp(self):
        janez = User.objects.create(username='Janez', password='geslo')
        Topic.objects.create(body='Recent topic', author=janez)
        Topic.objects.create(body='Old topic', author=janez, date=timezone.now()-datetime.timedelta(days=30))
        Comment.objects.create(topic=Topic.objects.get(body='Recent topic'), body='Comment', author=janez)

    def test_if_recent(self):
        recent_topic = Topic.objects.get(body='Recent topic')
        old_topic = Topic.objects.get(body='Old topic')

        self.assertIs(recent_topic.is_recent(), True)
        self.assertIs(old_topic.is_recent(), False)

    def test_if_comment_deleted(self):
        self.assertIs(Comment.objects.filter(body='Comment').count(), 1)
        Topic.objects.get(body='Recent topic').delete()
        self.assertIs(Comment.objects.filter(body='Comment').count(), 0)