from django.urls import path
from . import views

app_name = 'assessments'

urlpatterns = [
    path('take/<int:test_id>/', views.take_test, name='take_test'),
    path('results/', views.view_results, name='results'),
]
