from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count

from teachers.models import Teacher
from students.models import Student
from classes.models import SchoolClass

from .models import Activity
from classes.models import SchoolClass


@staff_member_required
def admin_dashboard(request):

    # Dashboard counts
    teacher_count = Teacher.objects.count()
    student_count = Student.objects.count()
    class_count = SchoolClass.objects.count()

    # Temporary until Worker module is created
    worker_count = 0

    # Recent activities
    activities = Activity.objects.order_by("-created_at")[:5]

    # -----------------------------
    # Student Gender Statistics
    # -----------------------------
    gender_data = (
        Student.objects
        .values("gender")
        .annotate(total=Count("id"))
    )

    gender_labels = [item["gender"] for item in gender_data]
    gender_values = [item["total"] for item in gender_data]

    # -----------------------------
    # Students Per Class Statistics
    # -----------------------------
    class_data = (
        Student.objects
        .values("school_class__name")
        .annotate(total=Count("id"))
        .order_by("school_class__name")
    )

    class_labels = [item["school_class__name"] for item in class_data]
    class_values = [item["total"] for item in class_data]

    context = {
        "teacher_count": teacher_count,
        "student_count": student_count,
        "worker_count": worker_count,
        "class_count": class_count,
        "activities": activities,

        # Chart data
        "gender_labels": gender_labels,
        "gender_values": gender_values,
        "class_labels": class_labels,
        "class_values": class_values,
    }

    return render(
        request,
        "dashboard/home.html",
        context,
    )