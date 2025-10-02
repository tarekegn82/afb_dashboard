from django.db import models
from django.conf import settings
from courses.models import Lesson


class Test(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='tests')
    title = models.CharField(max_length=200)
    instructions = models.TextField(blank=True)
    duration_minutes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f"{self.title} ({self.lesson.title})"


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    # simple MCQ: store options and correct index
    options = models.JSONField(default=list) # list of strings
    correct_index = models.IntegerField()


class Submission(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    answers = models.JSONField(default=dict)
    score = models.FloatField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)