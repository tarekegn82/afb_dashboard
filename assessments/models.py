from django.db import models
from django.contrib.auth.models import User
from courses.models import Lesson

class Test(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='tests')
    title = models.CharField(max_length=200)
    question = models.TextField()
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} ({self.lesson.title})"

class Submission(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    score = models.IntegerField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.test.title}"
