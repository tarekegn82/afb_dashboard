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
    # All lessons by this teacher
    lessons = Lesson.objects.filter(teacher=request.user)
    # Courses assigned to this teacher
    courses = Course.objects.filter(teacher=request.user)
    return render(request, 'courses/teacher_dashboard.html', {'lessons': lessons, 'courses': courses})

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
from django.shortcuts import render, get_object_or_404
from .models import Lesson

@login_required
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'courses/lesson_detail.html', {'lesson': lesson})

