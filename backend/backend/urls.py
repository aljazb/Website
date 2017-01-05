from django.conf.urls import include, url
from django.contrib import admin
from home import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^devices/', include('devices.urls')),
    url(r'^forum/', include('forum.urls')),
    url(r'^user/', include('users_app.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^', include('home.urls')),
    url(r'^$', include('home.urls')),
]
