from django import forms


class LoginForm (forms.Form):
    """Form to log users in"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
