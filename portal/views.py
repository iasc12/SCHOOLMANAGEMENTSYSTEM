from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



@login_required
def portal_redirect(request):

    user = request.user


    if user.role == "admin":

        return redirect(
            "admin_portal"
        )


    elif user.role == "teacher":

        return redirect(
            "teacher_portal"
        )


    elif user.role == "student":

        return redirect(
            "student_portal"
        )


    elif user.role == "worker":

        return redirect(
            "worker_portal"
        )


    else:

        return redirect(
            "login"
        )





@login_required
def admin_portal(request):

    return render(
        request,
        "portal/admin_portal.html"
    )




@login_required
def teacher_portal(request):

    from teachers.models import Teacher
    from students.models import Student


    teacher = Teacher.objects.get(
        user=request.user
    )


    assigned_classes = teacher.classes.all()


    total_classes = assigned_classes.count()


    total_students = Student.objects.filter(
        school_class__in=assigned_classes
    ).count()


    context = {

        "teacher": teacher,

        "assigned_classes": assigned_classes,

        "total_classes": total_classes,

        "total_students": total_students,

    }


    return render(
        request,
        "portal/teacher_portal.html",
        context
    )

@login_required
def student_portal(request):

    return render(
        request,
        "portal/student_portal.html"
    )





@login_required
def worker_portal(request):

    return render(
        request,
        "portal/worker_portal.html"
    )