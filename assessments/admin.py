from django.contrib import admin
from .models import Test, Submission

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('title','lesson')

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('test','student','score','submitted_at')
