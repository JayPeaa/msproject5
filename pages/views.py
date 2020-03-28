from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from pages.forms import LoginForm, RegistrationForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
# For views which don't have their own app, split out as you go.

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def contact_view(request):
    success = False
    if request.method == 'POST':
        send_mail(
            f"New Enquiry from {request.POST['emailaddress']}",
            request.POST['formmessage'],
            settings.DEFAULT_FROM_EMAIL,
            ['john.paul.hay.jph@gmail.com']
        )
        success = True
    return render(request, "contact.html", {'success': success})

