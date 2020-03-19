from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserProfileForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Congratulations {username}!  Your account has been created and you are now able to log in.')
            return redirect('login')
    else:
        registration_form = UserRegisterForm()
        profile_form = UserProfileForm()
    return render(request, 'users/register.html', {'registration_form': registration_form, 'profile_form': profile_form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

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