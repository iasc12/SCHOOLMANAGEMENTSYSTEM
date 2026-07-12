from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.class_list,
        name="class_list"
    ),

    path(
        "add/",
        views.add_class,
        name="add_class"
    ),

    path(
        "detail/<int:pk>/",
        views.class_detail,
        name="class_detail"
    ),

    path(
        "edit/<int:pk>/",
        views.edit_class,
        name="edit_class"
    ),

    path(
        "delete/<int:pk>/",
        views.delete_class,
        name="delete_class"
    ),
]