from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .models import SchoolClass
from .forms import SchoolClassForm


# ==========================
# CLASS LIST
# ==========================
def class_list(request):

    search = request.GET.get("search", "")

    classes = SchoolClass.objects.all().order_by("name")

    if search:
        classes = classes.filter(
            name__icontains=search
        )

    paginator = Paginator(classes, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "classes/class_list.html",
        {
            "classes": page_obj,
            "page_obj": page_obj,
            "search": search,
        },
    )


# ==========================
# ADD CLASS
# ==========================
def add_class(request):

    if request.method == "POST":

        form = SchoolClassForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("class_list")

    else:

        form = SchoolClassForm()

    return render(
        request,
        "classes/class_form.html",
        {
            "form": form,
        },
    )


# ==========================
# EDIT CLASS
# ==========================
def edit_class(request, pk):

    school_class = get_object_or_404(
        SchoolClass,
        pk=pk
    )

    if request.method == "POST":

        form = SchoolClassForm(
            request.POST,
            instance=school_class
        )

        if form.is_valid():
            form.save()
            return redirect("class_list")

    else:

        form = SchoolClassForm(
            instance=school_class
        )

    return render(
        request,
        "classes/class_form.html",
        {
            "form": form,
        },
    )


# ==========================
# DELETE CLASS
# ==========================
def delete_class(request, pk):

    school_class = get_object_or_404(
        SchoolClass,
        pk=pk
    )

    if request.method == "POST":

        school_class.delete()

        return redirect("class_list")

    return render(
        request,
        "classes/class_confirm_delete.html",
        {
            "school_class": school_class,
        },
    )


# ==========================
# CLASS DETAIL
# ==========================
def class_detail(request, pk):

    school_class = get_object_or_404(
        SchoolClass,
        pk=pk
    )

    return render(
        request,
        "classes/class_detail.html",
        {
            "school_class": school_class,
        },
    )