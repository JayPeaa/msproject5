from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from pages.forms import LoginForm, RegistrationForm, SubscriberForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Subscriber
from .forms import SubscriberForm
from django.db import models
from products.models import Product
from django.db.models import Count


# Create your views here.
# For views which don't have their own app, split out as you go.


def home_view(request):
    """Bestsellers logic and context for home view function runs
    on home page"""
    bestsellers = Product.objects.annotate(
        count_ordered=Count('orderlineitem')).order_by('-count_ordered')[:4]
    context = {
        'newsletter_form': SubscriberForm(),
        'bestsellers': bestsellers
    }
    return render(request, "home.html", context)


def contact_view(request):
    """Logic for contact form also returns newsletter context"""
    success = False
    if request.method == 'POST':
        send_mail(
            f"New Enquiry from {request.POST['emailaddress']}",
            request.POST['formmessage'],
            settings.DEFAULT_FROM_EMAIL,
            ['john.paul.hay@outlook.com']
        )
        success = True
        if success:
            messages.info(request, "Your message has been sent")
    context = {
        'newsletter_form': SubscriberForm(),
        'success': success
    }
    return render(request, "contact.html", context)


def subscribe_view(request):
    """Logic for subscribe form returns newsletter context"""
    newsletter_form = SubscriberForm(request.POST or None)
    if request.method == "POST":
        if newsletter_form.is_valid():
            subscriber_qs = Subscriber.objects.filter(
                email=newsletter_form.instance.email)
            if subscriber_qs.exists():
                messages.info(request, "You are already subscribed")
            else:
                newsletter_form.save()
                messages.info(request, "Thank you for subscribing")

    context = {
        'newsletter_form': SubscriberForm()
    }
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"), context)
