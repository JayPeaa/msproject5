from django.test import TestCase
from django.urls import reverse, resolve
from .models import Order, OrderLineItem
from users.models import Profile
from .views import checkout

# Create your tests here.


class test_url(TestCase):
    """Test urls are resolved"""

    def test_checkout_url_resolves(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout)


class BasicTest(TestCase):
    """Test product creation"""

    def test_fields(self):
        order = Order()
        order.order_total
        order.order_date
        order.order_full_name
        order.order_email
        order.order_phone_number
        order.order_street_address_1
        order.order_street_address_2
        order.order_city
        order.order_county
        order.order_country
        order.order_postcode
        order.save()
        record = Order.objects.get(id=1)
        self.assertEqual(record, order)
