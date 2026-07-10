from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):

    if request.method == "POST":
        username = request.POST['USERNAME']
        Password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            if user.role == "admin":
                return redirect('/admin/')
                
            elif user.role == "teacher":
                return redirect('/teacher-dashboard/')
            elif user.role == "student":
                return redirect('/student-dashboard/')
        return render(request, 'login.html')
                    