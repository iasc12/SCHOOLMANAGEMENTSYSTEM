from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Worker
from .forms import WorkerForm
from .models import Worker, WorkerTask


@login_required
def worker_dashboard(request):

    if request.user.role != "worker":
        return redirect("dashboard")

    worker = get_object_or_404(
        Worker,
        user=request.user
    )

    tasks = WorkerTask.objects.filter(
        worker=worker
    ).order_by("status", "due_date")

    pending = tasks.filter(status="Pending").count()
    completed = tasks.filter(status="Completed").count()

    return render(
        request,
        "workers/worker_dashboard.html",
        {
            "worker": worker,
            "tasks": tasks,
            "pending": pending,
            "completed": completed,
        },
    )

# ==========================================
# Worker Profile
# ==========================================

@login_required
def worker_profile(request):

    if request.user.role != "worker":
        return redirect("dashboard")

    worker = get_object_or_404(
        Worker,
        user=request.user
    )

    return render(
        request,
        "workers/worker_profile.html",
        {
            "worker": worker
        }
    )


# ==========================================
# Worker List
# ==========================================

@login_required
def worker_list(request):

    if not request.user.is_staff:
        return redirect("dashboard")

    workers = Worker.objects.all().order_by("employee_number")

    return render(
        request,
        "workers/worker_list.html",
        {
            "workers": workers
        }
    )


# ==========================================
# Add Worker
# ==========================================

@login_required
def add_worker(request):

    if not request.user.is_staff:
        return redirect("dashboard")

    if request.method == "POST":

        form = WorkerForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("worker_list")

        else:

            print("=" * 60)
            print("WORKER FORM ERRORS")
            print(form.errors)
            print("=" * 60)

    else:

        form = WorkerForm()

    return render(
        request,
        "workers/add_worker.html",
        {
            "form": form
        }
    )


# ==========================================
# Worker Details
# ==========================================

@login_required
def worker_detail(request, id):

    if not request.user.is_staff:
        return redirect("dashboard")

    worker = get_object_or_404(
        Worker,
        id=id
    )

    return render(
        request,
        "workers/worker_detail.html",
        {
            "worker": worker
        }
    )


# ==========================================
# Edit Worker
# ==========================================

@login_required
def edit_worker(request, id):

    if not request.user.is_staff:
        return redirect("dashboard")

    worker = get_object_or_404(
        Worker,
        id=id
    )

    if request.method == "POST":

        form = WorkerForm(
            request.POST,
            instance=worker
        )

        if form.is_valid():

            form.save()

            return redirect(
                "worker_detail",
                id=worker.id
            )

    else:

        form = WorkerForm(
            instance=worker
        )

    return render(
        request,
        "workers/edit_worker.html",
        {
            "form": form,
            "worker": worker
        }
    )


# ==========================================
# Delete Worker
# ==========================================

@login_required
def delete_worker(request, id):

    if not request.user.is_staff:
        return redirect("dashboard")

    worker = get_object_or_404(
        Worker,
        id=id
    )

    if request.method == "POST":

        worker.delete()

        return redirect("worker_list")

    return render(
        request,
        "workers/delete_worker.html",
        {
            "worker": worker
        }
    )