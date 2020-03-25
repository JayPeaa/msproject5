from django import forms
from .models import Order
from django.contrib.auth.models import User
from users.models import Profile, User
from orders.models import Order, OrderLineItem


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    cvv = forms.CharField(label='Security code (CVV)', 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    expiry_month = forms.ChoiceField(label='Month', 
        choices=MONTH_CHOICES, 
        required=False,
        widget=forms.Select(attrs={'class': 'form-control col-sm-5'}))
    expiry_year = forms.ChoiceField(label='Year', 
        choices=YEAR_CHOICES, 
        required=False,
        widget=forms.Select(attrs={'class': 'form-control col-sm-5'}))
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class UserOrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'order_full_name', 
            'order_email', 
            'order_phone_number', 
            'order_street_address_1', 
            'order_street_address_2', 
            'order_city', 
            'order_county', 
            'order_country', 
            'order_postcode' 
        ]
        labels = {
            'order_full_name' : 'Full Name',  
            'order_email' : 'Email',  
            'order_phone_number' : 'Phone Number',  
            'order_street_address_1' : 'Street Address Line 1',  
            'order_street_address_2' : 'Street Address Line 2',  
            'order_city' : 'City', 
            'order_county' : 'County',  
            'order_country' : 'Country', 
            'order_postcode' : 'Postcode'  
            
        }

class ProductOrderForm(forms.ModelForm):

    class Meta:
        model = OrderLineItem
        fields = [
            'product', 'quantity'
        ]