from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<show_count>[1-9]+[0-9]*)?$', views.home, name='home'),
    url(r'^(?P<show_count>[1-9]+[0-9]*)?/?show-more$', views.show_more, name='show_more'),
    url(r'^new-topic$', views.NewTopicFormView.as_view(), name='new_topic'),
]