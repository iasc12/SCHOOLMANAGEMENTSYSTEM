from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "admission_number",
        "first_name",
        "last_name",
        "gender",
        "school_class",
    )

    search_fields = (
        "admission_number",
        "first_name",
        "last_name",
    )

    list_filter = (
        "gender",
        "school_class",
    )