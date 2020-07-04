"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from myapp import views,views_volunteer,views_employee

urlpatterns = [
    path('', views.login),
    path('main', views.main),
    path('personal',views.personal),
    path('add_old',views.add_old),
    path('olds_info',views.olds_info),
    path('old_detail',views.old_detail),
    path('updatepassword',views.updatepassword), # 修改密码
    path('old_delete',views.old_delete), # 删除老人信息
    path('old_update',views.old_update),#修改老人信息
    path('old_analyze',views.old_analyze),#老人信息统计分析
    path('camara',views.camara),

    path('add_employee', views_employee.add_employee),
    path('add_volunteer', views_volunteer.add_volunteer),
    path('employees_info', views_employee.employees_info),
    path('volunteers_info', views_volunteer.volunteers_info),
    path('employee_detail', views_employee.employee_detail),
    path('volunteer_detail', views_volunteer.volunteer_detail),
    path('employee_update', views_employee.employee_update),
    path('volunteer_update', views_volunteer.volunteer_update),
    path('employee_analyze', views_employee.employee_analyze),
    path('volunteer_analyze', views_volunteer.volunteer_analyze),
    path('employee_delete', views_employee.employee_delete),
    path('volunteer_delete', views_volunteer.volunteer_delete),
]
