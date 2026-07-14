from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    list_display = (
        "employee_number",
        "first_name",
        "last_name",
        "email",
    )

    search_fields = (
        "employee_number",
        "first_name",
        "last_name",
    )

    filter_horizontal = (
        "classes",
    )