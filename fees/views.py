from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Fee, Payment
from .forms import FeeForm, PaymentForm

from classes.models import SchoolClass



@login_required
def fee_list(request):

    if request.user.role != "admin":
        return redirect("dashboard")


    search = request.GET.get("search")
    status_filter = request.GET.get("status")
    class_filter = request.GET.get("class")
    term_filter = request.GET.get("term")
    year_filter = request.GET.get("year")



    fees = Fee.objects.all().order_by("-created_at")



    # Search

    if search:

        fees = fees.filter(
            student__first_name__icontains=search
        ) | fees.filter(
            student__last_name__icontains=search
        ) | fees.filter(
            student__admission_number__icontains=search
        )



    # Cleared fees

    if status_filter == "cleared":

        fees = fees.filter(
            balance=0
        )



    # Fee balances

    elif status_filter == "balance":

        fees = fees.filter(
            balance__gt=0
        )



    # Class filter

    if class_filter:

        fees = fees.filter(
            student__school_class__id=class_filter
        )



    # Term filter

    if term_filter:

        fees = fees.filter(
            term=term_filter
        )



    # Year filter

    if year_filter:

        fees = fees.filter(
            year=year_filter
        )




    # =========================
    # FEE SUMMARY
    # =========================

    total_expected = sum(
        fee.amount for fee in fees
    )


    total_collected = sum(
        fee.amount_paid for fee in fees
    )


    total_balance = sum(
        fee.balance for fee in fees
    )





    # Pagination

    paginator = Paginator(
        fees,
        10
    )


    page_number = request.GET.get("page")


    page_obj = paginator.get_page(
        page_number
    )



    classes = SchoolClass.objects.all()



    return render(
        request,
        "fees/fee_list.html",
        {

            "page_obj": page_obj,

            "search": search,


            "classes": classes,

            "class_filter": class_filter,

            "term_filter": term_filter,

            "year_filter": year_filter,



            # Fee summary

            "total_expected": total_expected,

            "total_collected": total_collected,

            "total_balance": total_balance,

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

            return redirect(
                "fee_list"
            )



    else:

        form = FeeForm()



    return render(
        request,
        "fees/add_fee.html",
        {
            "form": form
        }
    )








@login_required
def fee_detail(request, pk):

    if request.user.role != "admin":
        return redirect("dashboard")


    fee = get_object_or_404(
        Fee,
        pk=pk
    )


    return render(
        request,
        "fees/fee_detail.html",
        {
            "fee": fee
        }
    )








@login_required
def edit_fee(request, pk):

    if request.user.role != "admin":
        return redirect("dashboard")


    fee = get_object_or_404(
        Fee,
        pk=pk
    )


    if request.method == "POST":

        form = FeeForm(
            request.POST,
            instance=fee
        )


        if form.is_valid():

            form.save()

            return redirect(
                "fee_list"
            )



    else:

        form = FeeForm(
            instance=fee
        )



    return render(
        request,
        "fees/edit_fee.html",
        {
            "form": form,
            "fee": fee
        }
    )








@login_required
def delete_fee(request, pk):

    if request.user.role != "admin":
        return redirect("dashboard")


    fee = get_object_or_404(
        Fee,
        pk=pk
    )


    if request.method == "POST":

        fee.delete()

        return redirect(
            "fee_list"
        )



    return render(
        request,
        "fees/delete_fee.html",
        {
            "fee": fee
        }
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

        form = PaymentForm(
            request.POST
        )


        if form.is_valid():

            payment = form.save(
                commit=False
            )


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

            "fee": fee
        }
    )@login_required
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



@login_required
def payment_receipt(request, pk):

    if request.user.role != "admin":
        return redirect("dashboard")


    payment = get_object_or_404(
        Payment,
        pk=pk
    )


    return render(
        request,
        "fees/receipt.html",
        {
            "payment": payment,
        }
    )