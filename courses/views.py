from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson
from django.contrib.auth.decorators import login_required
from .forms import LessonForm
from django.contrib import messages

def home(request):
    courses = Course.objects.all()
    return render(request, 'courses/home.html', {'courses': courses})

@login_required
def teacher_dashboard(request):
    # ensure teacher role
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'teacher':
        return redirect('courses:student_dashboard')
    courses = Course.objects.filter(teacher=request.user)
    return render(request, 'courses/teacher_dashboard.html', {'courses': courses})

@login_required
def student_dashboard(request):
    # show available lessons from all courses or enrolled ones (simple case: all)
    lessons = Lesson.objects.select_related('course').all()
    return render(request, 'courses/student_dashboard.html', {'lessons': lessons})

@login_required
def create_lesson(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.user.profile.role != 'teacher' or course.teacher != request.user:
        messages.error(request, 'Not allowed')
        return redirect('courses:teacher_dashboard')
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course
            lesson.save()
            messages.success(request, 'Lesson created.')
            return redirect('courses:teacher_dashboard')
    else:
        form = LessonForm()
    return render(request, 'courses/create_lesson.html', {'form': form, 'course': course})
