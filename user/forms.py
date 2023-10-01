from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'password1')