from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Fee, Payment
from .forms import FeeForm, PaymentForm

@login_required
def fee_list(request):

    if request.user.role != "admin":
        return redirect("dashboard")

    search = request.GET.get("search", "")

    fees = Fee.objects.all().order_by("-created_at")

    if search:
        fees = fees.filter(
            Q(student__first_name__icontains=search) |
            Q(student__last_name__icontains=search) |
            Q(student__admission_number__icontains=search)
        )

    paginator = Paginator(fees, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "fees/fee_list.html",
        {
            "page_obj": page_obj,
            "search": search,
        },
    )


@login_required
def add_fee(request):

    if request.user.role != "admin":
        return redirect("dashboard")

    if request.method == "POST":

        form = FeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("fee_list")

    else:
        form = FeeForm()

    return render(
        request,
        "fees/add_fee.html",
        {
            "form": form,
        },
    )


@login_required
def fee_detail(request, pk):

    if request.user.role != "admin":
        return redirect("dashboard")

    fee = get_object_or_404(Fee, pk=pk)

    return render(
        request,
        "fees/fee_detail.html",
        {
            "fee": fee,
        },
    )


@login_required
def edit_fee(request, pk):

    if request.user.role != "admin":
        return redirect("dashboard")

    fee = get_object_or_404(Fee, pk=pk)

    if request.method == "POST":

        form = FeeForm(
            request.POST,
            instance=fee
        )

        if form.is_valid():
            form.save()
            return redirect("fee_list")

    else:
        form = FeeForm(instance=fee)

    return render(
        request,
        "fees/edit_fee.html",
        {
            "form": form,
            "fee": fee,
        },
    )


@login_required
def delete_fee(request, pk):

    if request.user.role != "admin":
        return redirect("dashboard")

    fee = get_object_or_404(Fee, pk=pk)

    if request.method == "POST":

        fee.delete()

        return redirect("fee_list")

    return render(
        request,
        "fees/delete_fee.html",
        {
            "fee": fee,
        },
    )
@login_required
def add_payment(request, pk):

    if request.user.role != "admin":
        return redirect("dashboard")


    fee = get_object_or_404(
        Fee,
        pk=pk
    )


    if request.method == "POST":

        form = PaymentForm(request.POST)


        if form.is_valid():

            payment = form.save(commit=False)

            payment.fee = fee

            payment.save()


            return redirect(
                "fee_detail",
                pk=fee.id
            )


    else:

        form = PaymentForm()



    return render(
        request,
        "fees/add_payment.html",
        {
            "form": form,
            "fee": fee,
        }
    )