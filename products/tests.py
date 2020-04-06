from django.test import TestCase
from .models import Product
# Create your tests here.


class ProductTests(TestCase):
    """
    Run test against product models
    """

    def test_str(self):
        test_name = Product(product_name='New Product')
        self. assertEqual(str(test_name), 'New Product')
