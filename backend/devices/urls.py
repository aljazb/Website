from django.conf.urls import url
from . import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^brands$', views.brands, name='brands'),
    url(r'^top-rated$', views.top_rated, name='top-rated'),
    url(r'^just-released$', views.just_released, name='just-released'),
    url(r'^budget$', views.budget, name='budget'),
    url(r'^(?P<device_id>[0-9]+)(/(?P<show_count>[1-9]+[0-9]*))?$', views.device, name='detail'),
    url(r'^(?P<device_id>[0-9]+)(/(?P<show_count>[1-9]+[0-9]*))?/?show-more$', views.show_more, name='show_more'),
    url(r'^brands/(?P<brand_id>[0-9]+)$', views.brand, name='brand'),
    url(r'^', include('forum.urls')),
]