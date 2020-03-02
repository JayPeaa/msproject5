from django.conf.urls import url, include
from django.urls import path, include
from .views import products_view

#Not currently being used do I need to do this?

urlpatterns = [
    path('', products_view, name='products')
]