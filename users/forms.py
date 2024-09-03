from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Use 'email' instead of 'userEmail'

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]  # Use 'email' here as well
