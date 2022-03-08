from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def registerPage(request):
    return HttpResponse('Registration Page... ')

def loginPage(request):
    return HttpResponse('Login Page... ')

def logoutUser(request):
    return HttpResponse('Logout Page... ')