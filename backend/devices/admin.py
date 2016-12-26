from django.contrib import admin
from .models import Device, Brand, Os

admin.site.register(Device)
admin.site.register(Brand)
admin.site.register(Os)

