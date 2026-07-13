from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from accounts.models import CustomUser
from dashboard.models import Activity

from .models import Teacher
from .forms import TeacherProfileForm, AddTeacherForm


# ==========================
# Teacher Dashboard
# ==========================
@login_required
def teacher_dashboard(request):

    if request.user.role != "teacher":
        return redirect("dashboard")

    return render(
        request,
        "teachers/dashboard.html"
    )


# ==========================
# Teacher Profile
# ==========================
@login_required
def teacher_profile(request):

    teacher, created = Teacher.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = TeacherProfileForm(
            request.POST,
            instance=teacher
        )

        if form.is_valid():

            form.save()

            Activity.objects.create(
                user=request.user,
                message=f"{request.user.username} updated teacher profile"
            )

            return redirect("teacher_dashboard")

    else:

        form = TeacherProfileForm(
            instance=teacher
        )

    return render(
        request,
        "teachers/teacher_profile.html",
        {
            "form": form
        }
    )


# ==========================
# Teacher List
# ==========================
@staff_member_required
def teacher_list(request):

    teachers = Teacher.objects.all()

    return render(
        request,
        "teachers/teacher_list.html",
        {
            "teachers": teachers
        }
    )


# ==========================
# Add Teacher
# ==========================
@staff_member_required
def add_teacher(request):

    if request.method == "POST":

        form = AddTeacherForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.role = "teacher"
            user.is_staff = True
            user.save()

            Teacher.objects.create(
                user=user,
                employee_number=form.cleaned_data["employee_number"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                gender=form.cleaned_data["gender"],
                phone=form.cleaned_data["phone"],
                email=form.cleaned_data["email"],
            )

            Activity.objects.create(
                user=request.user,
                message=f"{request.user.username} added teacher {form.cleaned_data['first_name']} {form.cleaned_data['last_name']}"
            )

            return redirect("teacher_list")

    else:

        form = AddTeacherForm()

    return render(
        request,
        "teachers/add_teacher.html",
        {
            "form": form
        }
    )


# ==========================
# Teacher Detail
# ==========================
@staff_member_required
def teacher_detail(request, pk):

    teacher = get_object_or_404(
        Teacher,
        pk=pk
    )

    return render(
        request,
        "teachers/teacher_detail.html",
        {
            "teacher": teacher
        }
    )


# ==========================
# Edit Teacher
# ==========================
@staff_member_required
def teacher_edit(request, pk):

    teacher = get_object_or_404(
        Teacher,
        pk=pk
    )

    if request.method == "POST":

        form = TeacherProfileForm(
            request.POST,
            instance=teacher
        )

        if form.is_valid():

            form.save()

            Activity.objects.create(
                user=request.user,
                message=f"{request.user.username} updated teacher {teacher.first_name} {teacher.last_name}"
            )

            return redirect(
                "teacher_detail",
                pk=teacher.pk
            )

    else:

        form = TeacherProfileForm(
            instance=teacher
        )

    return render(
        request,
        "teachers/teacher_edit.html",
        {
            "form": form,
            "teacher": teacher,
        }
    )