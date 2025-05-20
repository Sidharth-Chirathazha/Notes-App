from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_http_methods
from .forms import UserRegistrationForm
import logging

logger = logging.getLogger(__name__)


def home_view(request):
    return render(request, 'home.html')


@require_http_methods(["GET", "POST"])
def register_view(request):

    if request.user.is_authenticated:
         return redirect('notes')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        else:
            logger.error(f"Registration failed: {form.errors}")
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.user.is_authenticated:
         return redirect('notes')

    if request.method == 'POST':
        user_email = request.POST.get('user_email')
        password = request.POST.get('password')

        user = authenticate(request, user_email=user_email, password=password)

        if user is not None:
            login(request, user)
            return redirect('notes')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


@login_required
@never_cache
def notes_view(request):
    return render(request, 'notes.html')