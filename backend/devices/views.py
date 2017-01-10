from django.shortcuts import render, redirect
from .models import Device, Os, Brand
from django.utils.translation import gettext_lazy as _

DEFAULT_TOPIC_COUNT = 5
EXPAND_COUNT = 5


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


def device(request, device_id, show_count=DEFAULT_TOPIC_COUNT):
    if show_count is None:
        show_count = DEFAULT_TOPIC_COUNT
    selected_device = Device.objects.get(id=device_id)
    selected_device.views += 1
    selected_device.save()
    context = {
        "device": selected_device,
        "topic_list": selected_device.topic_set.all()[:show_count],
    }

    return render(request, 'devices/details.html', context)


def show_more(request, device_id, show_count=DEFAULT_TOPIC_COUNT):
    if show_count is None:
        show_count = DEFAULT_TOPIC_COUNT
    return redirect('/devices/' + device_id + '/' + str(int(show_count)+EXPAND_COUNT))


def brand(request, brand_id):
    selected_brand = Brand.objects.get(id=brand_id)
    context = {
        "devices_list": selected_brand.device_set.all(),
        "category": selected_brand.name,
    }
    return render(request, 'devices/devices.html', context)


def top_rated(request):
    context = {
        "devices_list": Device.objects.order_by('-rating')[:10],
        "category": _("Top Rated"),
    }
    return render(request, 'devices/devices.html', context)


def just_released(request):
    context = {
        "devices_list": Device.objects.order_by('-date')[:10],
        "category": _("Just Released"),
    }
    return render(request, 'devices/devices.html', context)


def budget(request):
    context = {
        "devices_list": Device.objects.order_by('-price_rating')[:10],
        "category": _("Budget"),
    }
    return render(request, 'devices/devices.html', context)

