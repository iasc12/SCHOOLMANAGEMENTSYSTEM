from django.contrib import admin
from .models import SchoolClass


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "section",
        "created_at",
    )

    search_fields = (
        "name",
        "section",
    )