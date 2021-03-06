from django.contrib.auth.models import User
from django import forms


class RegisterForm(forms.ModelForm):
    """Form used for registering a user"""
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class LoginForm(forms.ModelForm):
    """Form used for logging in a user"""
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']