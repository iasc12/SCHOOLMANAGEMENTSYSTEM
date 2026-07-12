from django.contrib import admin
from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):

    list_display = (
        "message",
        "user",
        "created_at",
    )

    ordering = (
        "-created_at",
    )