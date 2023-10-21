from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'password'}),
        help_text=None
    )
    password2 = None  

    class Meta:
        model = CustomUser
        fields = ('username', 'password1' )
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'username'}),
        }

    def clean_password2(self):
        return self.cleaned_data.get("password1")