from __future__ import unicode_literals

from django.db import models
from brands.models import Brand
from datetime import datetime


class Device(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.now)
    performance_rating = models.IntegerField()
    build_rating = models.IntegerField()
    camera_rating = models.IntegerField()
    price_rating = models.IntegerField()
    dimensions = models.CharField(max_length=100)
    weight = models.CharField(max_length=50)
    display = models.CharField(max_length=100)
    os = models.CharField(max_length=50)
    chipset = models.CharField(max_length=100)
    memory = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)
    battery = models.CharField(max_length=100)

