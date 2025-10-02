from django.shortcuts import render, get_object_or_404, redirect
from .models import Test, Submission
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def take_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    if request.method == 'POST':
        student_answer = request.POST.get('answer','').strip()
        score = 1 if student_answer.lower() == test.correct_answer.lower() else 0
        Submission.objects.create(test=test, student=request.user, answer=student_answer, score=score)
        messages.success(request, f'You submitted the test. Score: {score}')
        return redirect('courses:student_dashboard')
    return render(request, 'assessments/take_test.html', {'test': test})

@login_required
def view_results(request):
    if request.user.profile.role == 'teacher':
        # teacher: show all submissions for their tests
        subs = Submission.objects.filter(test__lesson__course__teacher=request.user).select_related('test','student')
    else:
        subs = Submission.objects.filter(student=request.user).select_related('test')
    return render(request, 'assessments/results.html', {'submissions': subs})
