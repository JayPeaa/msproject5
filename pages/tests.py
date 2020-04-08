from django.test import TestCase
from .forms import LoginForm, SubscriberForm


# Create your tests here.

class TestLoginForm(TestCase):

    def test_user_name_is_required(self):
        form = LoginForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')

    def test_password_is_required(self):
        form = LoginForm({'password': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors.keys())
        self.assertEqual(form.errors['password'][0], 'This field is required.')


class TestSubscriberForm(TestCase):

    def test_email_is_required(self):
        form = SubscriberForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')
