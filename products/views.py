from django.shortcuts import render
from .models import Product

# Create your views here.
# This is the product listing page not the detail view 

def products_view(request, *args, **kwargs):
    obj= Product.objects.get(id=1)
    context ={
       'object': obj
    }
    return render(request, "products.html", context)

