from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUserView, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('activate/<uidb64>/<token>/', views.activateAccountView, name='activate'),

]
