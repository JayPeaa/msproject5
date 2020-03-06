from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
# This is the product listing page not the detail view 

def products_view(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def products_by_category_view(request, category):
    products = Product.objects.filter(product_category_id__category_name=category)
    return render(request, "products.html", {"products": products})

def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)

    return render(request, "product_detail.html", {"product": product})

