from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUserView, name='register'),
    path('login/', views.loginView, name='login'),
    path('dashboard/', views.dashboardView, name='dashboard'),
]
