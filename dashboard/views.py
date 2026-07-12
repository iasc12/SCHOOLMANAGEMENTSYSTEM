from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from teachers.models import Teacher
from students.models import Student


@staff_member_required
def admin_dashboard(request):
    teacher_count = Teacher.objects.count()
    student_count = Student.objects.count()

    # Temporary values until we create these modules
    worker_count = 0
    class_count = 0

    context = {
        "teacher_count": teacher_count,
        "student_count": student_count,
        "worker_count": worker_count,
        "class_count": class_count,
    }

    return render(
        request,
        "dashboard/home.html",
        context,
    )