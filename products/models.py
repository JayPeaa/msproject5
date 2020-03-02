from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    category_id = models.Field.primary_key=True
    category_name = models.TextField(max_length=30)
    def __str__(self):
        return self.category_name



class Product(models.Model):
    product_id = models.Field.primary_key=True
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_weight = models.DecimalField(max_digits=10, decimal_places=2)
    product_serves = models.IntegerField(blank=False)
    product_description = models.TextField(max_length=300)
    product_image = models.ImageField(upload_to="static/img", blank=True, null=True)
    product_category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_update_date = models.DateTimeField(auto_now_add=True)
    product_stock_qty = models.IntegerField(blank=False)
    product_live = models.BooleanField(default=True)
    def __str__(self):
        return self.product_name



