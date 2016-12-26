from django.shortcuts import render
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
    selected_device = Device.objects.get(id=device_id)
    selected_device.views += 1
    selected_device.save()
    context = {"device": selected_device}

    return render(request, 'devices/details.html', context)


def brand(request, brand_id):
    selected_brand = Brand.objects.get(id=brand_id)
    context = {
        "devices_list": selected_brand.device_set.all(),
        "category": selected_brand.name,
    }
    return render(request, 'devices/devices.html', context)


def top_rated(request):
    context = {
        "devices_list": Device.objects.order_by('-rating'),
        "category": "Top Rated",
    }
    return render(request, 'devices/devices.html', context)


def just_released(request):
    context = {
        "devices_list": Device.objects.order_by('-date'),
        "category": "Just Released",
    }
    return render(request, 'devices/devices.html', context)


def budget(request):
    context = {
        "devices_list": Device.objects.order_by('-price_rating'),
        "category": "Budget",
    }
    return render(request, 'devices/devices.html', context)

