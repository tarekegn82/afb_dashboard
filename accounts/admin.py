from django.contrib import admin
from .models import User, TeacherProfile, StudentProfile


admin.site.register(User)
admin.site.register(TeacherProfile)
admin.site.register(StudentProfile)