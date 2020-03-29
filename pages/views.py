from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from pages.forms import LoginForm, RegistrationForm, SubscriberForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Subscriber
from .forms import SubscriberForm


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
            ['john.paul.hay@outlook.com']
        )
        success = True
        if success:
            messages.info(request, "Your message has been sent")
    return render(request, "contact.html", {'success': success})

def subscribe_view(request):
    newsletter_form = SubscriberForm(request.POST or None)
    if request.method == "POST":
        if newsletter_form.is_valid():
            subscriber_qs = Subscriber.objects.filter(email=newsletter_form.instance.email)
            if subscriber_qs.exists():
                messages.info(request, "You are already subscribed")
            else:
                newsletter_form.save()

        context = {
            'newsletter_form' : newsletter_form
        }
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"),context)