from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register(requests):
    form = UserCreationForm()
    return render(requests, "users/register.html", {"form":form})

def login(requests):
    return render(requests, "users/login.html")    