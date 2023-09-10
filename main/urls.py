from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('', views.home, name='choose_login'),

    path('admin/', views.admin_login_view, name='admin_login'),

    path('lecturer/login', views.lecturer_login_view, name='lecturer_login'),
    path('lecturer/dashboard', views.lecturer_dashboard_view, name='lecturer_dashboard'),

    path('student/login', views.student_login_view, name='student_login'),
    path('student/dashboard', views.student_dashboard_view, name='student_dashboard'),

    path('logout', views.logout_view, name='logout'),
]
