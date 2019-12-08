from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def cart_view(request, *args, **kwargs):
    return render(request, "cart.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})


def products_view(request, *args, **kwargs):
    return render(request, "products.html", {})


def register_view(request, *args, **kwargs):
    return render(request, "register.html", {})


def logout_view(request, *args, **kwargs):
    """Logout User"""
    auth.logout(request)
    messages.success(
        request, "Thank you for visiting.  You are now logged out.")
    return redirect(reverse('home'))
