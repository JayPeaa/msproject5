from django.shortcuts import render, get_object_or_404
from .models import Product
from orders.models import Order
from pages.models import Subscriber
from pages.forms import SubscriberForm

# Create your views here.
# This is the product listing page not the detail view 

def products_view(request):
    products = Product.objects.all()
    context = {
        'newsletter_form' : SubscriberForm(),
        "products": products
    }
    return render(request, "products.html", context)

def products_by_category_view(request, category):
    products = Product.objects.filter(product_category_id__category_name=category)
    return render(request, "products.html", {"products": products})

def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        'newsletter_form' : SubscriberForm(),
        "product": product
    }

    return render(request, "product_detail.html", context)

def product_bestseller_view(request, id):
    bestsellers = Product.objects.annotate(count_ordered=Count('orderlineitem')).order_by('-count_ordered')[:4]

    return render(request, "product_detail.html", {"bestsellers": bestsellers})

