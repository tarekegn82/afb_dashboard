from django.contrib import admin
from .models import Course, Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','teacher')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title','course','created_at')
