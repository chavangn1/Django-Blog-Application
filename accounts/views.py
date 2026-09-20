from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from blogs.models import BlogPostsModel
from django.contrib.auth.decorators import login_required
from .models import User
from .tokens import account_activation_token

from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

# Create your views here.

def registerUserView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()
            messages.success(request, 'You have registered successfully, check your inbox for a link to activate your account')
            return redirect('login')
        else:
            messages.error(request, "Please correct the above errors.")

    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def activateAccountView(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your account is activated. You can log in now.")
    else:
        messages.error(request, "This activation link is invalid or has expired.")

    return redirect('login')



def loginView(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            next_url = request.POST.get('next')
            return redirect(next_url) if next_url else redirect('dashboard')
        else:
            # authenticate() returns None both for wrong credentials AND
            # for correct credentials on an inactive account.
            try:
                existing_user = User.objects.get(email=email)
                if not existing_user.is_active:
                    messages.error(request, "Please activate your account first — check your email for the link.")
                else:
                    messages.error(request, "Invalid email or password. Please try again.")
            except User.DoesNotExist:
                messages.error(request, "Invalid email or password. Please try again.")

    return render(request, 'accounts/login.html')

def logoutView(request):
    logout(request)
    return redirect('login')

@login_required
def dashboardView(request):
    blogs = BlogPostsModel.objects.filter(author = request.user)
    return render(request, 'accounts/dashboard.html', {'blogs': blogs})
