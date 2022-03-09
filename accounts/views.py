from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
from .forms import UserForm, MyUserCreationForm

# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
    else:
        return render(request, 'register.html')
def loginPage(request):
    return render(request, 'login.html')

def logoutUser(request):
    return HttpResponse('Logout Page... ')