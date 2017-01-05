from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<topic_id>[0-9]+)$', views.topic, name='topic'),
    url(r'^(?P<topic_id>[0-9]+)/heart$', views.topic_heart, name='topic_heart'),
    url(r'^comment/(?P<comment_id>[0-9]+)/heart$', views.comment_heart, name='comment_heart'),
    url(r'^([0-9]+/)?new-topic/(?P<device_id>[0-9]+)$', views.new_topic, name='new_topic'),
    url(r'^(?P<topic_id>[0-9]+)/delete$', views.delete_topic, name='topic_delete'),
    url(r'^comment/(?P<comment_id>[0-9]+)/delete$', views.delete_comment, name='comment_delete'),
]