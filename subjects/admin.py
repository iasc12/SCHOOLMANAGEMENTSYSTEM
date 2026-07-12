from django.contrib import admin
from .models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
        "teacher",
        "is_compulsory",
    )

    list_filter = (
        "is_compulsory",
    )

    search_fields = (
        "name",
        "code",
    )

    filter_horizontal = (
        "classes",
    )