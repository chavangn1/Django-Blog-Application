from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from blogs.models import BlogPostsModel
from django.contrib.auth.decorators import login_required

# Create your views here.

def registerUserView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'You have registered successfully')
            return redirect('login')
        else:
            messages.error(request, "Please correct the above errors.")

    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def loginView(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            # messages.success(request, "You have logged in successfully!")
            
            next_url = request.POST.get('next')

            if next_url:
                return redirect(next_url)
            
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid email or password. Please try again.")

    return render(request, 'accounts/login.html')

def logoutView(request):
    logout(request)
    return redirect('login')

@login_required
def dashboardView(request):
    blogs = BlogPostsModel.objects.filter(author = request.user)
    return render(request, 'accounts/dashboard.html', {'blogs': blogs})
