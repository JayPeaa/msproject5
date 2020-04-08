from django.test import TestCase
from django.urls import reverse, resolve
from .views import register, profile
# Create your tests here.


class test_url(TestCase):
    """Test urls are resolved"""

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_profile_view_url_resolves(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)
