from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# ==========================
# LOGIN VIEW
# ==========================

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            if user.role == "admin":
                return redirect("admin_dashboard")

            elif user.role == "teacher":
                return redirect("teacher_dashboard")

            elif user.role == "student":
                return redirect("student_dashboard")

            elif user.role == "worker":
                return redirect("worker_dashboard")

            else:
                return redirect("dashboard")

        return render(
            request,
            "accounts/login.html",
            {
                "error": "Invalid username or password"
            }
        )

    return render(request, "accounts/login.html")


# ==========================
# LOGOUT
# ==========================

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


# ==========================
# DASHBOARD REDIRECT
# ==========================

@login_required
def dashboard_redirect(request):
    role = request.user.role

    if role == "admin":
        return redirect("admin_dashboard")

    elif role == "teacher":
        return redirect("teacher_dashboard")

    elif role == "student":
        return redirect("student_dashboard")

    elif role == "worker":
        return redirect("worker_dashboard")

    return redirect("login")


# ==========================
# ADMIN DASHBOARD
# ==========================

@login_required
def admin_dashboard(request):
    if request.user.role != "admin":
        return redirect("dashboard")

    return render(request, "accounts/admin_dashboard.html")


# ==========================
# TEACHER DASHBOARD
# ==========================

@login_required
def teacher_dashboard(request):
    if request.user.role != "teacher":
        return redirect("dashboard")

    return render(request, "accounts/teacher_dashboard.html")


# ==========================
# STUDENT DASHBOARD
# ==========================

@login_required
def student_dashboard(request):
    if request.user.role != "student":
        return redirect("dashboard")

    return render(request, "accounts/student_dashboard.html")


# ==========================
# WORKER DASHBOARD
# ==========================

@login_required
def worker_dashboard(request):
    if request.user.role != "worker":
        return redirect("dashboard")

    return render(request, "accounts/worker_dashboard.html")