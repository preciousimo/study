from django.urls import path
from . import views

urlpatterns = [
    # Path to login
    path('login/', views.loginPage, name="login"),
    
    # path to logout
    path('logout/', views.logoutUser, name="logout"),

    # path to registration
    path('register/', views.registerPage, name="register"),    
]
