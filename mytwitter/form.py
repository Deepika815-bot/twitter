from django import forms
from .models import Usertwitter
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UsertwitterFrom(forms.ModelForm):
    class Meta:
        model=Usertwitter
        fields=["text","photo"]     



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    model = User
    fields = ("username", "email", "password1", "password2")
