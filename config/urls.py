from django.contrib import admin
from django.urls import path, include
from accounts import views as account_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Authentication
    path("login/", account_views.login_view, name="login"),
    path("logout/", account_views.logout_view, name="logout"),

    # Dashboard
    path("dashboard/", account_views.dashboard_redirect, name="dashboard"),

    # Role dashboards
    path("admin-dashboard/", account_views.admin_dashboard, name="admin_dashboard"),
    path("teacher-dashboard/", account_views.teacher_dashboard, name="teacher_dashboard"),
    path("student-dashboard/", account_views.student_dashboard, name="student_dashboard"),
    path("worker-dashboard/", account_views.worker_dashboard, name="worker_dashboard"),

    # Students app
    path("students/", include("students.urls")),
]