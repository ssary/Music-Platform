
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('loginUser/', views.loginUser, name='loginUser'),
]