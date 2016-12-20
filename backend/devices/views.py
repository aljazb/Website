from django.http import HttpResponse


def devices(request):
    return HttpResponse("<h1>Devices</h1>")
