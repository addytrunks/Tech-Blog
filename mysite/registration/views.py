from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistrationForm


# Create your views here.
class UserRegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('reg:login')
