from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # set role on profile
            role = form.cleaned_data['role']
            user.profile.role = role
            user.profile.save()
            messages.success(request, 'Account created. Please log in.')
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.profile.role == 'teacher':
                return redirect('courses:teacher_dashboard')
            return redirect('courses:student_dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'accounts/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('courses:home')
