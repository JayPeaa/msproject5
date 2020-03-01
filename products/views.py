from django.shortcuts import render
from .models import Product

# Create your views here.
# This is the product listing page not the detail view 

def products_view(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


