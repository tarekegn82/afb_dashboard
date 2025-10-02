from django.shortcuts import render, redirect
from .models import Test, Submission

def take_test(request, test_id):
    test = Test.objects.get(id=test_id)
    if request.method == 'POST':
        student_answer = request.POST['student_answer']
        score = 1 if student_answer.lower() == test.answer.lower() else 0
        Submission.objects.create(
            student=request.user,
            test=test,
            student_answer=student_answer,
            score=score
        )
        return redirect('student_dashboard')
    return render(request, 'assessments/take_test.html', {'test': test})
