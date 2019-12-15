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


def login_view(request, *args, **kwargs):
    """Login a User"""
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You are now logged in.")
                return redirect(reverse('home'))
            else:
                login_form.add_error(None, "Incorrect username or password!")
    else:
        login_form = LoginForm()

    return render(request, "login.html", {"login_form": login_form})


def products_view(request, *args, **kwargs):
    return render(request, "products.html", {})


def register_view(request, *args, **kwargs):
    """Registration page rendering"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('home'))
            else:
                message.error(
                    request, "Registration unsucccesful please try again")
    else:
        registration_form = RegistrationForm()
    return render(request, "register.html", {"registration_form": registration_form})


@login_required  # not sure if this is working ceck url patterns.
def logout_view(request, *args, **kwargs):
    """Logout User"""
    auth.logout(request)
    messages.success(
        request, "Thank you for visiting.  You are now logged out.")
    return redirect(reverse('home'))

def profile_view(request):
    """User profile page"""
    user=User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})