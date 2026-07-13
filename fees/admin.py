from django.contrib import admin
from .models import Fee


@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "term",
        "year",
        "amount",
        "amount_paid",
        "balance",
        "status",
    )

    list_filter = (
        "status",
        "term",
        "year",
    )

    search_fields = (
        "student__first_name",
        "student__last_name",
        "student__admission_number",
    )