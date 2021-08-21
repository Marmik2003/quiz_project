from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

from .models import User
from .forms import RegistrationForm


def signup(request):
    if request.method == 'POST':
        print(request.POST)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=raw_password)
            login(request, user)
            return redirect('student:index')

    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method != 'POST':
        return render(request, 'login.html')
    else:
        email = request.POST['email']
        password = request.POST['pass']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_authenticated:
                if user.is_superuser:
                    return redirect('test_admin:dashboard')
                else:
                    return redirect('student:index')
            else:
                messages.error(request, 'Invalid credentials!')
                return redirect('users:login')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('users:login')


def logout_view(request):
    request.session.flush()
    logout(request)
    return HttpResponseRedirect('/')
