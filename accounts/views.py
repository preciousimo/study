from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from base.models import User
from .forms import UserForm, MyUserCreationForm
from base.EmailBackEnd import EmailBackEnd
from base import urls

# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "{} created successfully".format(username))
            return redirect('/login')
        else:
            messages.error(request, "Failed to register user")
            return redirect('/register')
    else:
        form = MyUserCreationForm(request.POST)
        return render(request, 'register.html', {'form':form})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = EmailBackEnd.authenticate(request, username=username,password=password)
        if user != None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/login')

    return render(request, 'login.html')

def logoutUser(request):
    return HttpResponse('Logout Page... ')