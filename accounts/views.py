from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def registerPage(request):
    return render(request, 'register.html')

def loginPage(request):
    return render(request, 'login.html')

def logoutUser(request):
    return HttpResponse('Logout Page... ')