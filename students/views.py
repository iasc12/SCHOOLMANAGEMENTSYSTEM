from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .models import Student
from .forms import StudentForm

from dashboard.models import Activity



def student_list(request):

    search = request.GET.get("search", "")

    students = Student.objects.all()


    if search:

        students = students.filter(
            admission_number__icontains=search
        ) | students.filter(
            first_name__icontains=search
        ) | students.filter(
            last_name__icontains=search
        )


    paginator = Paginator(
        students,
        10
    )

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(
        page_number
    )


    return render(
        request,
        "students/student_list.html",
        {
            "students": page_obj,
            "page_obj": page_obj,
            "search": search,
        }
    )




def add_student(request):

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES
        )


        if form.is_valid():

            student = form.save()


            Activity.objects.create(
                user=request.user,
                message=f"{request.user.username} added student {student.first_name} {student.last_name}"
            )


            return redirect(
                "student_list"
            )


    else:

        form = StudentForm()


    return render(
        request,
        "students/student_form.html",
        {
            "form": form
        }
    )





def edit_student(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )


    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES,
            instance=student
        )


        if form.is_valid():

            student = form.save()


            Activity.objects.create(
                user=request.user,
                message=f"{request.user.username} updated student {student.first_name} {student.last_name}"
            )


            return redirect(
                "student_list"
            )


    else:

        form = StudentForm(
            instance=student
        )


    return render(
        request,
        "students/student_form.html",
        {
            "form": form
        }
    )





def delete_student(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )


    if request.method == "POST":

        Activity.objects.create(
            user=request.user,
            message=f"{request.user.username} deleted student {student.first_name} {student.last_name}"
        )


        student.delete()


        return redirect(
            "student_list"
        )


    return render(
        request,
        "students/student_confirm_delete.html",
        {
            "student": student
        }
    )





def student_detail(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )


    return render(
        request,
        "students/student_detail.html",
        {
            "student": student
        }
    )