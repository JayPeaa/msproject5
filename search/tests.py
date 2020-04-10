from django.test import TestCase
from django.urls import reverse, resolve
from .views import do_search

# Create your tests here.


class test_url(TestCase):
    """Test urls are resolved"""

    def test_search_url_resolves(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, do_search)
