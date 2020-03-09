from django.conf.urls import url, include
from .views import view_cart, add_to_cart, adjust_cart, delete_cart_item
from django.urls import path, include

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add/<id>/', add_to_cart, name='add_to_cart'),
    path('adjust/<id>/', adjust_cart, name='adjust_cart'),
    path('delete/<id>/', delete_cart_item, name='delete_cart_item'),
]


# update to path before subit