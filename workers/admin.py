from django.contrib import admin
from .models import Worker, WorkerTask


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):

    list_display = (
        "employee_number",
        "first_name",
        "last_name",
        "job_title",
        "phone",
    )

    search_fields = (
        "employee_number",
        "first_name",
        "last_name",
    )


@admin.register(WorkerTask)
class WorkerTaskAdmin(admin.ModelAdmin):

    list_display = (
        "worker",
        "title",
        "status",
        "due_date",
        "created_at",
    )

    list_filter = (
        "status",
        "due_date",
    )

    search_fields = (
        "title",
        "worker__first_name",
        "worker__last_name",
    )