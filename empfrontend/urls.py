from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmpList,name='employee-list-front'),
    path('employeedetail/<int:pk>/', views.EmpDetail,name='employee-detail-front'),
    path('addemployee/', views.EmpCreate,name='add-employee'),
    path('updateemployee/<int:pk>/', views.EmpUpdate,name='update-employee'),
    path('deleteinactive/', views.DeleteInactive,name='delete-inactive'),
    path('updatesalary/', views.UpdateSalary,name='update-salary'),
    path('updatestatus/<int:pk>/', views.UpdateStatus,name='update-status'),

    
]
