from django.urls import path
from . import views


urlspatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_redirect, name='dashboard'),

    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('teacher_dashboard/', views.admin_dashboard, name='teacher_dashboard'),
    path('student_dashboard/', views.admin_dashboard, name='student_dashboard'),
    path('worker_dashboard/', views.admin_dashboard, name='worker_dashboard'),

]