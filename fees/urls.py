from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.fee_list,
        name="fee_list",
    ),

    path(
        "add/",
        views.add_fee,
        name="add_fee",
    ),

    path(
        "detail/<int:pk>/",
        views.fee_detail,
        name="fee_detail",
    ),

    path(
        "edit/<int:pk>/",
        views.edit_fee,
        name="edit_fee",
    ),

    path(
        "delete/<int:pk>/",
        views.delete_fee,
        name="delete_fee",
    ),
    path(
    "payment/<int:pk>/",
    views.add_payment,
    name="add_payment",
),

]