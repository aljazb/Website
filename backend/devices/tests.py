from django.test import TestCase
from .models import Device, Brand, Os


class DeviceTest(TestCase):
    """Class representing tests connected to the device app"""
    def setUp(self):
        """Method that sets up all of the objects used in the test class"""
        android = Os.objects.create(name='Android')
        ios = Os.objects.create(name='iOS')
        windows = Os.objects.create(name='Windows Phone')
        apple = Brand.objects.create(os=ios, name='Apple')
        google = Brand.objects.create(os=android, name='Google')
        nokia = Brand.objects.create(os=windows, name='Nokia')
        Device.objects.create(brand=google, name='Pixel', description='',
                                image='', rating=5, performance_rating=5,
                                build_rating=5, camera_rating=5, price_rating=5,
                                dimensions='', weight='', display='', os='', chipset='',
                                memory='', camera='', battery='', views=0)
        Device.objects.create(brand=apple, name='iPhone', description='',
                                image='', rating=3, performance_rating=5,
                                build_rating=5, camera_rating=5, price_rating=4,
                                dimensions='', weight='', display='', os='', chipset='',
                                memory='', camera='', battery='', views=0)
        Device.objects.create(brand=nokia, name='Lumia', description='',
                                image='', rating=5, performance_rating=5,
                                build_rating=5, camera_rating=4, price_rating=4,
                                dimensions='', weight='', display='', os='', chipset='',
                                memory='', camera='', battery='', views=0)

    def test_device_os(self):
        """Tests whether the is_running_android method is working"""
        android_device = Device.objects.get(name="Pixel")
        ios_device = Device.objects.get(name="iPhone")
        windows_device = Device.objects.get(name="Lumia")

        self.assertIs(android_device.is_running_android(), True)
        self.assertIs(ios_device.is_running_android(), False)
        self.assertIs(windows_device.is_running_android(), False)

    def test_device_rating(self):
        """Tests whether the rating methods are working"""
        android_device = Device.objects.get(name="Pixel")
        ios_device = Device.objects.get(name="iPhone")
        windows_device = Device.objects.get(name="Lumia")

        self.assertIs(android_device.rating_score_rounded(), 5)
        self.assertIs(ios_device.rating_score_rounded(), 4)
        self.assertIs(windows_device.rating_score_rounded(), 5)

