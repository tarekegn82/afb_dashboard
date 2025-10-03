from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson
from .forms import LessonForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    courses = Course.objects.all()
    return render(request, 'courses/home.html', {'courses': courses})

@login_required
def teacher_dashboard(request):
    # Courses created by this teacher
    courses = Course.objects.filter(teacher=request.user)
    # Lessons from those courses
    lessons = Lesson.objects.filter(course__in=courses)
    return render(request, 'courses/teacher_dashboard.html', {
        'courses': courses,
        'lessons': lessons
    })

@login_required
def student_dashboard(request):
    # Show all lessons (or filter by enrolled courses if implemented)
    lessons = Lesson.objects.select_related('course').all()
    return render(request, 'courses/student_dashboard.html', {'lessons': lessons})

@login_required
def create_lesson(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    # Only the teacher who owns this course can create lessons
    if request.user.profile.role != 'teacher' or course.teacher != request.user:
        messages.error(request, 'You are not allowed to add lessons to this course.')
        return redirect('courses:teacher_dashboard')

    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course
            lesson.save()
            messages.success(request, f'Lesson "{lesson.title}" created for course "{course.title}".')
            return redirect('courses:teacher_dashboard')
    else:
        form = LessonForm()

    return render(request, 'courses/create_lesson.html', {'form': form, 'course': course})
@login_required
def create_course(request):
    if request.user.profile.role != 'teacher':
        messages.error(request, "Only teachers can create courses.")
        return redirect('courses:student_dashboard')

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        course = Course.objects.create(
            title=title,
            description=description,
            teacher=request.user  # 👈 assign the logged-in teacher
        )
        messages.success(request, f'Course "{course.title}" created successfully.')
        return redirect('courses:teacher_dashboard')

    return render(request, 'courses/create_course.html')

@login_required
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'courses/lesson_detail.html', {'lesson': lesson})
