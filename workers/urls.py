from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.worker_list,
        name="worker_list",
    ),

    path(
        "dashboard/",
        views.worker_dashboard,
        name="worker_dashboard",
    ),

    path(
        "profile/",
        views.worker_profile,
        name="worker_profile",
    ),

    path(
        "add/",
        views.add_worker,
        name="add_worker",
    ),

    path(
        "detail/<int:id>/",
        views.worker_detail,
        name="worker_detail",
    ),

    path(
        "edit/<int:id>/",
        views.edit_worker,
        name="edit_worker",
    ),

    path(
        "delete/<int:id>/",
        views.delete_worker,
        name="delete_worker",
    ),
]