from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
# Create your views here.

def registerUserView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'You have registered successfully')
            return redirect('register')
        else:
            messages.error(request, "Please correct the errors below.")

    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def loginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in successfully!")
            return redirect('dashboard')  # redirect to your dashboard/home page
        else:
            messages.error(request, "Invalid email or password. Please try again.")

    return render(request, 'accounts/login.html')

def dashboardView(request):
    return HttpResponse(f"You have came to dashboard - {request.user}")
