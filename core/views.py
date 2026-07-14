from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import School
from .forms import SchoolForm


@login_required
def school_profile(request):

    if request.user.role != "admin":
        return redirect("dashboard")

    school = School.objects.first()

    if request.method == "POST":

        if school:
            form = SchoolForm(
                request.POST,
                request.FILES,
                instance=school,
            )
        else:
            form = SchoolForm(
                request.POST,
                request.FILES,
            )

        if form.is_valid():

            school = form.save()

            messages.success(
                request,
                "School profile saved successfully."
            )

            return redirect("school_profile")

        else:

            messages.error(
                request,
                "Please correct the errors below."
            )

    else:

        form = SchoolForm(
            instance=school
        )

    return render(
        request,
        "core/school_profile.html",
        {
            "form": form,
            "school": school,
        },
    )