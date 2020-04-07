from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserRegisterForm, UserProfileForm, UserUpdateForm
from .forms import ProfileUpdateForm

# Create your views here.


def register(request):
    """Aditional fields for user form linked to profile object to register"""
    if request.method == 'POST':

        user_form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'username': request.POST['username'],
            'password1': request.POST['password1'],
            'password2': request.POST['password2']
        }

        user_profile_data = {
            'user_phone_number': request.POST['user_phone_number'],
            'user_city': request.POST['user_city'],
            'user_street_address_1': request.POST['user_street_address_1'],
            'user_street_address_2': request.POST['user_street_address_2'],
            'user_county': request.POST['user_county'],
            'user_country': request.POST['user_country'],
            'user_postcode': request.POST['user_postcode']
        }

        user_form = UserRegisterForm(user_form_data)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            profile = Profile.objects.get(user__username=username)
            profile_form = UserProfileForm(user_profile_data, instance=profile)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request,
                                 f'Account Created {username}, Please log in')
            return redirect('login')
    else:
        registration_form = UserRegisterForm()
        profile_form = UserProfileForm()
    return render(request,
                  'users/register.html',
                  {'registration_form': registration_form,
                   'profile_form': profile_form})


@login_required
def profile(request):
    """Update profile information when logged in"""
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,
                             f'Your account information has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/profile.html', context)


def profile_view(request):
    """User profile page"""
    user = User.objects.get(email=request.user.email)
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
