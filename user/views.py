from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUser
from .forms import CustomUserForm


class Create(generic.CreateView):
    model = CustomUser
    form_class = CustomUserForm
    success_url = reverse_lazy('#')


class Thanks(generic.TemplateView):
    template_name = 'user/thanks.html'

# Create your views here.
