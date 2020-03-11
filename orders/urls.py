from django.urls import include, path
from .views import checkout

urlpatterns = [
    path('orders/', checkout, name='checkout')
]