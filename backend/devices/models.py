from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class Os(models.Model):
    """Class representing the Os object

    This class represents the operating system of a device, it is a mandatory foreign key in Brand class
    """
    name = models.CharField(max_length=50);

    def __str__(self):
        """String representation of Os"""
        return self.name


class Brand(models.Model):
    """Class representing the Brand object

    This class represents the brand of a device, it is a mandatory foreign key in Device class
    """
    os = models.ForeignKey(Os, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100);

    def __str__(self):
        """String representation of Brand"""
        return self.name


class Device(models.Model):
    """Class representing the Device object"""
    PHONE = 'PH'
    TABLET = 'TB'
    DEVICE_TYPE = (
        (PHONE, 'Phone'),
        (TABLET, 'Tablet'),
    )

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.now)
    rating = models.IntegerField()
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
    views = models.IntegerField(default=0)
    type = models.CharField(max_length=2, choices=DEVICE_TYPE, default=PHONE)

    def __str__(self):
        """String representation of Device"""
        return self.name

    def is_running_android(self):
        """Returns True if device is running Android"""
        return self.brand.os.name == 'Android'

    def rating_score(self):
        """Calculates the average score of the device

        The overall score has a weight of 3, all others have a weight of 1
        The function returns a float
        """
        return (self.rating * 3 + self.performance_rating + self.camera_rating + self.build_rating + self.price_rating)/7.

    def rating_score_rounded(self):
        """Rounds the returned value of rating_score function and returnes it"""
        return int(round(self.rating_score()))
