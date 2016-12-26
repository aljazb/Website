from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^brands$', views.brands, name='brands'),
    url(r'^top-rated$', views.TopRatedView.as_view(), name='top-rated'),
    url(r'^just-released$', views.JustReleasedView.as_view(), name='just-released'),
    url(r'^budget$', views.BudgetView.as_view(), name='budget'),
    url(r'^(?P<device_id>[0-9]+)$', views.device, name='detail'),
    url(r'^brands/(?P<brand_id>[0-9]+)$', views.brand, name='brand'),
]