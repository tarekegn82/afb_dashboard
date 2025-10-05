from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Test, Submission
from courses.models import Lesson


@login_required
def create_test(request, lesson_id):
    """Teacher creates a test for a specific lesson."""
    if request.user.profile.role != 'teacher':
        messages.error(request, "Only teachers can create tests.")
        return redirect('courses:teacher_dashboard')

    lesson = get_object_or_404(Lesson, id=lesson_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        question = request.POST.get('question')
        correct_answer = request.POST.get('correct_answer')
        if title and question and correct_answer:
            Test.objects.create(
                lesson=lesson,
                title=title,
                question=question,
                correct_answer=correct_answer
            )
            messages.success(request, "Test created successfully!")
            return redirect('assessments:view_lesson_tests', lesson_id=lesson.id)
        else:
            messages.error(request, "All fields are required.")

    return render(request, 'assessments/create_test.html', {'lesson': lesson})


@login_required
def view_lesson_tests(request, lesson_id):
    """Teacher views all tests for a specific lesson."""
    if request.user.profile.role != 'teacher':
        return redirect('courses:student_dashboard')

    lesson = get_object_or_404(Lesson, id=lesson_id)
    tests = lesson.tests.all()  # Use the correct related_name from Test model

    return render(request, 'assessments/view_lesson_tests.html', {
        'lesson': lesson,
        'tests': tests
    })


@login_required
def available_tests(request):
    """Students see all available tests."""
    if request.user.profile.role != 'student':
        return redirect('courses:teacher_dashboard')

    tests = Test.objects.all()
    return render(request, 'assessments/available_tests.html', {'tests': tests})


@login_required
def take_test(request, test_id):
    """Students take a specific test."""
    if request.user.profile.role != 'student':
        return redirect('courses:teacher_dashboard')

    test = get_object_or_404(Test, id=test_id)

    if request.method == 'POST':
        answer = request.POST.get('answer', '').strip()
        score = 1 if answer.lower() == test.correct_answer.lower() else 0
        Submission.objects.create(
            test=test,
            student=request.user,
            answer=answer,
            score=score
        )
        messages.success(request, f"Submitted! Your score: {score}")
        return redirect('assessments:results')

    return render(request, 'assessments/take_test.html', {'test': test})


@login_required
def results(request):
    """View test submissions."""
    if request.user.profile.role == 'teacher':
        # Teacher sees all submissions for their courses
        submissions = Submission.objects.filter(test__lesson__course__teacher=request.user)
    else:
        # Student sees only their own submissions
        submissions = Submission.objects.filter(student=request.user)

    return render(request, 'assessments/results.html', {'submissions': submissions})
