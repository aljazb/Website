from django.shortcuts import render
from forum.models import Topic
from devices.models import Device


def home(request):
    topics = Topic.objects.filter(device=None)
    popular_phones = Device.objects.filter(type=Device.PHONE).order_by('-views')[:5]
    popular_tablets = Device.objects.filter(type=Device.TABLET).order_by('-views')[:5]
    context = {
        "topics": topics,
        "popular_phones": popular_phones,
        "popular_tablets": popular_tablets,
    }
    return render(request, 'home/index.html', context)
