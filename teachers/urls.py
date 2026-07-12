from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("profile/", views.teacher_profile, name="teacher_profile"),
    path("list/", views.teacher_list, name="teacher_list"),
    path("detail/<int:pk>/", views.teacher_detail, name="teacher_detail"),
    path(
    "edit/<int:pk>/",
    views.teacher_edit,
    name="teacher_edit",
),
]