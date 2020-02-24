from django.contrib import admin

# Register your models here.
from .models import Product
from .models import ProductCategory

admin.site.register(Product)
admin.site.register(ProductCategory)
