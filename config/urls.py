from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from accounts import views as account_views


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),


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


    path(
        "dashboard/",
        account_views.dashboard_redirect,
        name="dashboard"
    ),


    path(
        "admin-dashboard/",
        include("dashboard.urls")
    ),


    path(
        "teacher-dashboard/",
        account_views.teacher_dashboard,
        name="teacher_dashboard"
    ),


    path(
        "student-dashboard/",
        account_views.student_dashboard,
        name="student_dashboard"
    ),


    path(
        "worker-dashboard/",
        account_views.worker_dashboard,
        name="worker_dashboard"
    ),


    path(
        "students/",
        include("students.urls")
    ),


    path(
        "teachers/",
        include("teachers.urls")
    ),

]


if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )