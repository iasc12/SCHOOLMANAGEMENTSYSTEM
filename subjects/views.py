from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

from .models import Subject
from .forms import SubjectForm

from dashboard.models import Activity


@staff_member_required
def subject_list(request):

    subjects = Subject.objects.all().order_by("name")

    return render(
        request,
        "subjects/subject_list.html",
        {
            "subjects": subjects,
        },
    )


@staff_member_required
def add_subject(request):

    if request.method == "POST":

        form = SubjectForm(request.POST)

        if form.is_valid():

            subject = form.save()

            Activity.objects.create(
                user=request.user,
                message=f"{request.user.username} added subject {subject.name}",
            )

            return redirect("subject_list")

    else:

        form = SubjectForm()

    return render(
        request,
        "subjects/subject_form.html",
        {
            "form": form,
        },
    )


@staff_member_required
def subject_detail(request, pk):

    subject = get_object_or_404(
        Subject,
        pk=pk,
    )

    return render(
        request,
        "subjects/subject_detail.html",
        {
            "subject": subject,
        },
    )


@staff_member_required
def edit_subject(request, pk):

    subject = get_object_or_404(
        Subject,
        pk=pk,
    )

    if request.method == "POST":

        form = SubjectForm(
            request.POST,
            instance=subject,
        )

        if form.is_valid():

            subject = form.save()

            Activity.objects.create(
                user=request.user,
                message=f"{request.user.username} updated subject {subject.name}",
            )

            return redirect(
                "subject_detail",
                pk=subject.pk,
            )

    else:

        form = SubjectForm(
            instance=subject,
        )

    return render(
        request,
        "subjects/subject_form.html",
        {
            "form": form,
        },
    )


@staff_member_required
def delete_subject(request, pk):

    subject = get_object_or_404(
        Subject,
        pk=pk,
    )

    if request.method == "POST":

        Activity.objects.create(
            user=request.user,
            message=f"{request.user.username} deleted subject {subject.name}",
        )

        subject.delete()

        return redirect("subject_list")

    return render(
        request,
        "subjects/subject_confirm_delete.html",
        {
            "subject": subject,
        },
    )