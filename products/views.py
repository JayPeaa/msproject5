from django.shortcuts import render, get_object_or_404
from .models import Product
from pages.forms import SubscriberForm

# Create your views here.
# This is the product listing page not the detail view


def products_view(request):
    """Getting all product for store and also returning newsletter
    form as context for the subscribe field"""
    products = Product.objects.all()
    context = {
        'newsletter_form': SubscriberForm(),
        "products": products
    }
    return render(request, "products.html", context)


def products_by_category_view(request, category):
    """Filters for product categories"""
    products = Product.objects.filter(
        product_category_id__category_name=category)
    return render(request, "products.html", {"products": products})


def product_detail_view(request, id):
    """Product detail view and newsletter as context"""
    product = get_object_or_404(Product, id=id)
    context = {
        'newsletter_form': SubscriberForm(),
        "product": product
    }

    return render(request, "product_detail.html", context)


def product_bestseller_view(request, id):
    """Dynamic updating for top 4 bestsellers on home page"""
    bestsellers = Product.objects.annotate(
        count_ordered=Count('orderlineitem')).order_by('-count_ordered')[:4]

    return render(request, "product_detail.html", {"bestsellers": bestsellers})
