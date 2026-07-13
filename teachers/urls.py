from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.teacher_list,
        name="teacher_list",
    ),

    path(
        "add/",
        views.add_teacher,
        name="add_teacher",
    ),

    path(
        "dashboard/",
        views.teacher_dashboard,
        name="teacher_dashboard",
    ),

    path(
        "profile/",
        views.teacher_profile,
        name="teacher_profile",
    ),

    path(
        "detail/<int:pk>/",
        views.teacher_detail,
        name="teacher_detail",
    ),

    path(
        "edit/<int:pk>/",
        views.teacher_edit,
        name="teacher_edit",
    ),

]