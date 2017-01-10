from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    url(r'^devices/', include('devices.urls')),
    url(r'^forum/', include('forum.urls')),
    url(r'^user/', include('users_app.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^', include('home.urls')),
    url(r'^$', include('home.urls')),
)

