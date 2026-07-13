from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from accounts import views as account_views


urlpatterns = [

    # ==========================
    # Django Admin
    # ==========================
    path(
        "admin/",
        admin.site.urls
    ),

    # ==========================
    # Authentication
    # ==========================
    path(
        "login/",
        account_views.login_view,
        name="login"
    ),

    path(
        "logout/",
        account_views.logout_view,
        name="logout"
    ),

    # ==========================
    # Dashboard Redirect
    # ==========================
    path(
        "dashboard/",
        account_views.dashboard_redirect,
        name="dashboard"
    ),

    # ==========================
    # Admin Dashboard
    # ==========================
    path(
        "admin-dashboard/",
        include("dashboard.urls")
    ),

    # ==========================
    # Teacher Dashboard
    # ==========================
    path(
        "teacher-dashboard/",
        account_views.teacher_dashboard,
        name="teacher_dashboard"
    ),

    # ==========================
    # Student Dashboard
    # ==========================
    path(
        "student-dashboard/",
        account_views.student_dashboard,
        name="student_dashboard"
    ),

    # ==========================
    # Worker Dashboard
    # ==========================
    path(
        "worker-dashboard/",
        account_views.worker_dashboard,
        name="worker_dashboard"
    ),

    # ==========================
    # Students
    # ==========================
    path(
        "students/",
        include("students.urls")
    ),

    # ==========================
    # Teachers
    # ==========================
    path(
        "teachers/",
        include("teachers.urls")
    ),

    # ==========================
    # Subjects
    # ==========================
    path(
        "subjects/",
        include("subjects.urls")
    ),

    # ==========================
    # Classes
    # ==========================
    path(
        "classes/",
        include("classes.urls")
    ),

    # ==========================
    # Workers
    # ==========================
    path(
        "workers/",
        include("workers.urls")
    ),

]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)