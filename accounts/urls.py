from django.urls import path
from . import views

urlpatterns = [
    # Login and logout
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # Dashboard redirect (decides where each user goes)
    path("dashboard/", views.dashboard_redirect, name="dashboard"),

    # Individual dashboards
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("teacher-dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("student-dashboard/", views.student_dashboard, name="student_dashboard"),
    path("worker-dashboard/", views.worker_dashboard, name="worker_dashboard"),
]