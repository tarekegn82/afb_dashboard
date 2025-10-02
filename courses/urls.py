from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.home, name='home'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('course/<int:course_id>/create_lesson/', views.create_lesson, name='create_lesson'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),  # 👈 Add this
]
