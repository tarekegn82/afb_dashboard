from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Lesson

def home(request):
    return render(request, 'courses/home.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect("teacher_dashboard")
            else:
                return redirect("student_dashboard")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "courses/login.html")

def teacher_dashboard(request):
    lessons = Lesson.objects.filter(teacher=request.user)
    return render(request, 'courses/teacher_dashboard.html', {'lessons': lessons})

def student_dashboard(request):
    lessons = Lesson.objects.all()
    return render(request, 'courses/student_dashboard.html', {'lessons': lessons})
