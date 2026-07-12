from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


# ==========================
# STUDENT LIST
# ==========================
def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        "students/student_list.html",
        {"students": students},
    )


# ==========================
# ADD STUDENT
# ==========================
def add_student(request):

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("student_list")

    else:
        form = StudentForm()

    return render(
        request,
        "students/student_form.html",
        {"form": form},
    )


# ==========================
# EDIT STUDENT
# ==========================
def edit_student(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect("student_list")

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        "students/student_form.html",
        {"form": form},
    )


# ==========================
# DELETE STUDENT
# ==========================
def delete_student(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
    return render(
    request,
    "students/student_confirm_delete.html",
    {"student": student},
)