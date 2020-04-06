from django.db import models
from products.models import Product
from users.models import Profile


# Create your models here.
class Order(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, related_name="orders",
        null=True, blank=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_full_name = models.CharField(max_length=50, null=False, blank=False)
    order_email = models.EmailField(max_length=254, null=False,
                                    blank=False, default='')
    order_phone_number = models.CharField(max_length=20,
                                          null=False, blank=False)
    order_street_address_1 = models.CharField(max_length=60, blank=False)
    order_street_address_2 = models.CharField(max_length=60, blank=False)
    order_city = models.CharField(max_length=40, blank=False)
    order_county = models.CharField(max_length=40, blank=False)
    order_country = models.CharField(max_length=40, blank=False)
    order_postcode = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return f'{self.order_full_name}-{self.order_postcode}'


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return f'{self.quantity}-{self.product}'
