from django.test import TestCase
from django.urls import reverse, resolve
from .models import Product, ProductCategory
from products.views import products_view, products_by_category_view, product_detail_view

# Create your tests here.


class ProductTests(TestCase):
    """Product name test"""

    def test_str(self):
        test_name = Product(product_name='Pork chops')
        self.assertEqual(str(test_name), 'Pork chops')


class test_url(TestCase):
    """Test urls are resolved"""

    def test_product_url_resolves(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func, products_view)

    def test_product_category_url_resolves(self):
        url = reverse('products_by_category', args=['path'])
        self.assertEquals(resolve(url).func, products_by_category_view)
    
    def test_product_detail_view_url_resolves(self):
        url = reverse('product_detail_view', args=['path'])
        self.assertEquals(resolve(url).func, product_detail_view)


class BasicTest(TestCase):
    """Check fields post"""

    def test_fields(self):
        category = ProductCategory(category_name="Pork")
        category.save()
        product = Product()
        product.category_name = category
        product.product_category = category
        product.product_name = "Test Product"
        product.product_price = 2.99
        product.product_weight = 350
        product.product_serves = 4
        product.product_description = "A new test product"
        product.product_image_name = "donkey.jpg"
        product.product_stock_qty = 10
        product.product_live = True
        product.save()
        record = Product.objects.get(id=1)
        self.assertEqual(record, product)
