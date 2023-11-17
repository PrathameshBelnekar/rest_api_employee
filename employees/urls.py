from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmpList.as_view(),name='employee-list'),
    path('employee/<int:pk>/', views.EmpDetail.as_view(),name='employee-detail'),
    path('updatedeletesalary/', views.UpdateDeleteSalary.as_view() , name='update-delete-salary')
]




