from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login_form, name='login'),
    url(r'^login/redirect/$', views.login_form, name='login'),
    url(r'^login/redirect/(?P<redirect_link>[a-zA-Z0-9/-]+)$', views.login_form, name='login_redirect'),
    url(r'^register$', views.RegisterFormView.as_view(), name='register'),
    url(r'^logout$', views.logout_user, name='logout'),
    url(r'^logout/redirect/(?P<redirect_link>[a-zA-Z0-9/-]+)$', views.logout_user, name='logout_redirect'),
    url(r'^logout/redirect/$', views.logout_user, name='logout'),
]