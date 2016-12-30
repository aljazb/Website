from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.LoginFormView.as_view(), name='login'),
    url(r'^register$', views.RegisterFormView.as_view(), name='register'),
    url(r'^logout$', views.logout_user, name='logout'),
]