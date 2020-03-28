from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from pages.forms import LoginForm, RegistrationForm
from django.core.mail import send_mail


# Create your views here.
# For views which don't have their own app, split out as you go.

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def contact_view(request):
    if request.method == 'POST':
        send_mail(
            "New Enquiry",
            request.POST['formmessage'],
            request.POST['emailaddress'],
            ['john.paul.hay@outlook.com']
        )
    return render(request, "contact.html", {})

