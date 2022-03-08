from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, Logout
from django.contrib import messages


# Create your views here.
def registerPage(request):
    return HttpResponse('Registration Page... ')

def loginPage(request):
    return HttpResponse('Login Page... ')

def logoutUser(request):
    return HttpResponse('Logout Page... ')