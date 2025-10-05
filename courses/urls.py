from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.home, name='home'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('course/<int:course_id>/create_lesson/', views.create_lesson, name='create_lesson'),
    path('create_course/', views.create_course, name='create_course'),
    
    # 👇 Add this line for lesson detail
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),

    # For Assessments
    path('create-test/', views.create_test, name='create_test'),
    path('take-test/', views.take_test, name='take_test'),
    # add results if needed
    path('results/', views.results, name='results'),
]
