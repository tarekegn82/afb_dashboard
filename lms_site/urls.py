from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("courses.urls")),           # homepage + dashboards
    path("accounts/", include("accounts.urls")), # login, logout, register
    path("assessments/", include("assessments.urls")),
]
