from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.portal_redirect,
        name="portal"
    ),


    path(
        "admin/",
        views.admin_portal,
        name="admin_portal"
    ),


    path(
        "teacher/",
        views.teacher_portal,
        name="teacher_portal"
    ),


    path(
        "student/",
        views.student_portal,
        name="student_portal"
    ),


    path(
        "worker/",
        views.worker_portal,
        name="worker_portal"
    ),

]