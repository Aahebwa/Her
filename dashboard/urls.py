from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.index, name='index'),
    path('department/', views.home, name="home"),
    path('upload/', views.upload_file, name='upload_file'),
    path('department/IT/computer_science/', views.computer_science, name='computer_science'),
    path('department/IT/computer_science/course_units/', views.course_unit, name='file_list'),
    path('department/IT/computer_science/course_units/add',views.add_course_unit, name='add_course_unit'),
    path('accounts/login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('department/IT/', views.it, name='it'),
    path('department/ELECTRONICS/', views.electr, name='electronics'),
    path('logout/', views.logout_view, name='logout'),
    path('department/IT/computer_science/course_units/<slug:slug>', views.details, name="details"),
]
