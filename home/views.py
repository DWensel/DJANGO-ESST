from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect


class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'

    # Override the get function
    def get(self, request, *args, **kwargs): 
        if self.request.user.is_authenticated: # Checks if the user is already logged in
            return redirect('notes.list') 
        return super().get(request, *args, **kwargs) # This line is what GET already does


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'
    # Upon successful login, Django has a default redirect set to /accounts/profile/. We changed this in settings.py


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


class AuthoerizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'