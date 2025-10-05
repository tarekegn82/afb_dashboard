from django.urls import path
from . import views

app_name = 'assessments'

urlpatterns = [
    path('lesson/<int:lesson_id>/create_test/', views.create_test, name='create_test'),
    path('lesson/<int:lesson_id>/tests/', views.view_lesson_tests, name='view_lesson_tests'),
    path('test/<int:test_id>/take/', views.take_test, name='take_test'),
    path('results/', views.results, name='results'),
]
