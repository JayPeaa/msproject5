from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from pages.forms import LoginForm, RegistrationForm

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def cart_view(request, *args, **kwargs):
    return render(request, "cart.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def products_view(request, *args, **kwargs):
    return render(request, "products.html", {})

def profile_view(request):
    """User profile page"""
    user=User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})

def password_reset_view(request):
    """password reset view"""
    return render(request, 'pasword_reset.html', {})

def password_reset_done_view(request):
    """password reset, email link to change password"""
    return render(request, 'pasword_reset_done.html', {})

def password_reset_confirm_view(request):
    """password reset, email link to change password"""
    return render(request, 'pasword_reset_confirm.html', {})