from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from rent_management.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')  # Replace 'home' with your desired URL name
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, "rent/base/login.html")


def user_logout(request):
    logout(request)
    return redirect('/')
