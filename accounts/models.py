from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
# add a role field
    ROLE_CHOICES = (
    ('teacher', 'Teacher'),
    ('student', 'Student'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')


class TeacherProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)


class StudentProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=50, blank=True, null=True)