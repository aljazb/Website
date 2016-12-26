from django.conf.urls import include, url
from django.contrib import admin
from home import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^devices/', include('devices.urls')),
    url(r'^forum/', include('forum.urls')),
    url(r'^home$', views.home, name='home'),
    url(r'^$', views.home),
]
