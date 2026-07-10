from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Redirect users according to their role
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

        else:
            return render(request, "accounts/login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "accounts/login.html")


# Logout view
@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


# Main dashboard redirect
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

    else:
        return redirect("login")


# Admin dashboard
@login_required
def admin_dashboard(request):
    return render(request, "accounts/admin_dashboard.html")


# Teacher dashboard
@login_required
def teacher_dashboard(request):
    return render(request, "accounts/teacher_dashboard.html")


# Student dashboard
@login_required
def student_dashboard(request):
    return render(request, "accounts/student_dashboard.html")


# Worker dashboard
@login_required
def worker_dashboard(request):
    return render(request, "accounts/worker_dashboard.html")