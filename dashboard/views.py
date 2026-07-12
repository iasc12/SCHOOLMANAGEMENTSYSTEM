from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from teachers.models import Teacher
from students.models import Student

from .models import Activity



@staff_member_required
def admin_dashboard(request):


    teacher_count = Teacher.objects.count()


    student_count = Student.objects.count()


    # Temporary until modules are created

    worker_count = 0

    class_count = 0



    activities = Activity.objects.all()[:5]



    context = {

        "teacher_count": teacher_count,

        "student_count": student_count,

        "worker_count": worker_count,

        "class_count": class_count,

        "activities": activities,

    }



    return render(

        request,

        "dashboard/home.html",

        context

    )