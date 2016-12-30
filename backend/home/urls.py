from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^new-topic$', views.NewTopicFormView.as_view(), name='home'),
]