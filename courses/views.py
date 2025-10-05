from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Lesson
from .forms import LessonForm
from assessments.models import Test, Submission

def home(request):
    courses = Course.objects.all()
    return render(request, 'courses/home.html', {'courses': courses})


@login_required
def teacher_dashboard(request):
    # Courses created by this teacher
    courses = Course.objects.filter(teacher=request.user)
    # Lessons from those courses
    lessons = Lesson.objects.filter(course__in=courses)
    # Tests belonging to teacher's lessons
    tests = Test.objects.filter(lesson__in=lessons)

    return render(request, 'courses/teacher_dashboard.html', {
        'courses': courses,
        'lessons': lessons,
        'tests': tests
    })


@login_required
def student_dashboard(request):
    # Show all lessons (or filter by enrolled courses if implemented)
    lessons = Lesson.objects.select_related('course').all()
    # Show all tests for available lessons
    tests = Test.objects.select_related('lesson').all()

    return render(request, 'courses/student_dashboard.html', {
        'lessons': lessons,
        'tests': tests
    })


@login_required
def create_lesson(request, course_id):
    course = get_object_or_404(Course, id=course_id)
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
            teacher=request.user
        )
        messages.success(request, f'Course "{course.title}" created successfully.')
        return redirect('courses:teacher_dashboard')

    return render(request, 'courses/create_course.html')


@login_required
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    # Include tests for this lesson
    tests = Test.objects.filter(lesson=lesson)
    return render(request, 'courses/lesson_detail.html', {'lesson': lesson, 'tests': tests})

def view_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'course/lesson_detail.html', {'lesson': lesson})

# Optional placeholders for compatibility, can be removed if using assessments app directly
@login_required
def create_test(request, lesson_id=None):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return redirect('assessments:create_test', lesson_id=lesson.id)


@login_required
def take_test(request, test_id=None):
    return redirect('assessments:take_test', test_id=test_id)


@login_required
def results(request):
    return redirect('assessments:results')
