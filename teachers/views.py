from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .forms import TeacherProfileForm
from .models import Teacher


@login_required
def teacher_dashboard(request):
    return render(request, "teachers/dashboard.html")


@login_required
def teacher_profile(request):
    teacher, created = Teacher.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = TeacherProfileForm(request.POST, instance=teacher)

        if form.is_valid():
            form.save()
            return redirect("teacher_dashboard")

    else:
        form = TeacherProfileForm(instance=teacher)

    return render(
        request,
        "teachers/teacher_profile.html",
        {"form": form},
    )


@staff_member_required
def teacher_list(request):
    teachers = Teacher.objects.all()

    return render(
        request,
        "teachers/teacher_list.html",
        {"teachers": teachers},
    )


@staff_member_required
def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    return render(
        request,
        "teachers/teacher_detail.html",
        {"teacher": teacher},
    )


@staff_member_required
def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == "POST":
        form = TeacherProfileForm(request.POST, instance=teacher)

        if form.is_valid():
            form.save()
            return redirect("teacher_detail", pk=teacher.pk)

    else:
        form = TeacherProfileForm(instance=teacher)

    return render(
        request,
        "teachers/teacher_edit.html",
        {
            "form": form,
            "teacher": teacher,
        },
    )