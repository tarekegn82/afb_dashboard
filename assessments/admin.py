from django.contrib import admin
from .models import Test, Question, Submission


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'duration_minutes', 'created_at')
    search_fields = ('title',)
    list_filter = ('lesson',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'test', 'correct_index')
    search_fields = ('text',)
    list_filter = ('test',)


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('test', 'student', 'score', 'submitted_at')
    list_filter = ('test', 'student')