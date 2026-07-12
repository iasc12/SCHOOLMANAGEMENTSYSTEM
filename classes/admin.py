from django.contrib import admin
from .models import SchoolClass


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'stream',
        'academic_year',
    )