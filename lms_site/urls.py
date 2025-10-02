from django.contrib import admin
from django.urls import path
from courses import views
from assessments.views import take_test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('test/<int:test_id>/', take_test, name='take_test'),
]
