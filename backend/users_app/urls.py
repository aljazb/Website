from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.UserFormView.as_view(), name='register'),
]