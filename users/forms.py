from django import forms
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username',
                  'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )
        labels = {
            'user_phone_number': 'Phone Number',
            'user_city': 'City',
            'user_street_address_1': 'Address Line 1',
            'user_street_address_2': 'Addres Line 2',
            'user_county': 'County',
            'user_country': 'Country',
            'user_postcode': 'Postal Code'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_phone_number'].widget.attrs['pattern'] = "[0-9]{1,15}"


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_street_address_1', 'user_street_address_2',
                  'user_city', 'user_county', 'user_country',
                  'user_county', 'user_postcode', 'user_phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_phone_number'].widget.attrs['pattern'] = "[0-9]{1,15}"
