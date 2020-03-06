from django.conf.urls import url, include
from django.urls import path, include
from .views import products_view, products_by_category_view, product_detail_view

#Not currently being used do I need to do this?

urlpatterns = [
    path('', products_view, name='products'),
    path('category/<category>', products_by_category_view, name='products_by_category'),
    path('product/<id>', product_detail_view, name='product_detail_view')
]