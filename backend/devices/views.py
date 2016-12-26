from django.shortcuts import render
from django.views import generic
from .models import Device, Os, Brand


def brands(request):
    android = Os.objects.get(name='Android')
    ios = Os.objects.get(name='iOS')
    windows = Os.objects.get(name='Windows Phone')
    other = Os.objects.get(name='Other')
    context = {
        'android_list_left': android.brand_set.all()[:5],
        'android_list_right': android.brand_set.all()[5:],
        'ios_list': ios.brand_set.all(),
        'windows_list': windows.brand_set.all(),
        'other_list_left': other.brand_set.all()[:2],
        'other_list_right': other.brand_set.all()[2:],
    }
    return render(request, 'devices/brands.html', context)


def device(request, device_id):
    context = {"device": Device.objects.get(id=device_id)}
    return render(request, 'devices/details.html', context)


def brand(request, brand_id):
    selected_brand = Brand.objects.get(id=brand_id)
    context = {"devices_list": selected_brand.device_set.all()}
    return render(request, 'devices/devices.html', context)


class TopRatedView(generic.ListView):
    template_name = 'devices/devices.html'
    context_object_name = 'devices_list'

    def get_queryset(self):
        return Device.objects.order_by('-rating')


class JustReleasedView(generic.ListView):
    template_name = 'devices/devices.html'
    context_object_name = 'devices_list'

    def get_queryset(self):
        return Device.objects.order_by('-date')


class BudgetView(generic.ListView):
    template_name = 'devices/devices.html'
    context_object_name = 'devices_list'

    def get_queryset(self):
        return Device.objects.order_by('-price_rating')
