from email.message import EmailMessage
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.conf import settings
from django.core.mail import send_mail

from django.views import View
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
# Create your views here.
class SingUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"