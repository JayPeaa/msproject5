from django.db import models
from products.models import Product

# Create your models here.
class Order(models.Model):
    order_product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    order_qty = models.IntegerField(blank=False)
  
    
