from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        role = request.POST.get('role')

        # Validate fields
        if not all([username, email, password1, password2, role]):
            messages.error(request, "All fields are required.")
            return redirect('accounts:register')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('accounts:register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('accounts:register')

        if role not in ['teacher', 'student']:
            messages.error(request, "Invalid role selection.")
            return redirect('accounts:register')

        # Create user safely
        user = User.objects.create_user(username=username, email=email, password=password1)
        profile, created = Profile.objects.get_or_create(user=user)
        profile.role = role
        profile.save()


        messages.success(request, "Account created successfully. Please login.")
        return redirect('accounts:login')

    return render(request, 'accounts/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            role = user.profile.role
            if role == 'teacher':
                return redirect('courses:teacher_dashboard')
            else:
                return redirect('courses:student_dashboard')
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'accounts/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('courses:home')

