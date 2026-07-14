from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),


    # Authentication
    path(
        "",
        include("accounts.urls")
    ),


    # Portal system
    path(
        "portal/",
        include("portal.urls")
    ),


    # Existing apps
    path(
        "students/",
        include("students.urls")
    ),


    path(
        "teachers/",
        include("teachers.urls")
    ),


    path(
        "workers/",
        include("workers.urls")
    ),


    path(
        "fees/",
        include("fees.urls")
    ),


    path(
        "subjects/",
        include("subjects.urls")
    ),


    path(
        "exams/",
        include("exams.urls")
    ),

]


if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )