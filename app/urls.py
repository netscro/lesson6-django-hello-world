"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from home.views import home, main_page, students, student_update,\
    students_info, student_update_main

urlpatterns = [

    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('', main_page, name='main_page'),
    path('students/', students, name='students'),
    path('student-update/<id>/', student_update, name='student_update'),
    path('student-update/', student_update_main, name='student_update_main'),
    path('students-info/', students_info, name='students_info'),

]
