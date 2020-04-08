from django.test import TestCase
from django.urls import reverse, resolve
from .views import view_cart, add_to_cart, adjust_cart, delete_cart_item

# Create your tests here.


class test_url(TestCase):
    """Test urls are resolved"""

    def test_view_cart_url_resolves(self):
        url = reverse('view_cart')
        self.assertEquals(resolve(url).func, view_cart)

    def test_add_to_cart_url_resolves(self):
        url = reverse('add_to_cart', args=['path'])
        self.assertEquals(resolve(url).func, add_to_cart)

    def test_adjust_cart_view_url_resolves(self):
        url = reverse('adjust_cart', args=['path'])
        self.assertEquals(resolve(url).func, adjust_cart)

    def test_delete_cart_item_view_url_resolves(self):
        url = reverse('delete_cart_item', args=['path'])
        self.assertEquals(resolve(url).func, delete_cart_item)
