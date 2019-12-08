from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from pages.forms import LoginForm

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def cart_view(request, *args, **kwargs):
    return render(request, "cart.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def login_view(request, *args, **kwargs):
    """Login a User"""
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You are now logged in.")
            else:
                login_form.add_error(None, "Incorrect username or password!")
    else:
        login_form = LoginForm()

    return render(request, "login.html", {"login_form": login_form})


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
