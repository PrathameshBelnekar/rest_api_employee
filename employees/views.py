from . models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import EmpSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.utils import timezone

"""
1)	Perform CRUD Operation in DJango Rest Framework.
2)	Create table employee_name , And add fields (emp_name, joining_date,salary,status(active/deactive)
3)	Create API to Update salary whos completed recently one year. And Delete employees which having deactive status.
"""

class EmpList(APIView):
#send a get request to employees/ to get list of employees
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmpSerializer(employees , many= True)
        return Response(serializer.data)

#send a post request to employees/ wtih data to add a new employee
    def post(self, request):
        serializer = EmpSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


#send get request with id to employee/id/ to get a single employee
class EmpDetail(APIView):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmpSerializer(employee)
        return Response(serializer.data)
    
#send put request with id and data to employee/id/ to update a single employee
    def put(self, request , pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmpSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
#send delete request with id to employee/id/ to delete a single employee
    def delete(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        



        
#send get request to updatedeletesalary/ to list all employees
class UpdateDeleteSalary(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmpSerializer(employees , many= True)
        return Response(serializer.data)

#send a put request to updatedeletesalary/ to update the salary of employees completed 1 year
    def put(self, request):
        duration = timezone.now() - timezone.timedelta(days=365)
        print(duration)
        employees = Employee.objects.filter(joining_date__lte=duration)

        for emp in employees:
            print(emp)
            emp.salary = emp.salary + 5000
            emp.save()
        return Response({"message" : "updated successfully"})
    
#send a delete request to updatedeletesalary/ to delete employees marked as deactive
    def delete(self, request):
        inactive_emp = Employee.objects.filter(status = 'Deactive')
        inactive_emp.delete()
        return Response({"message" : "deleted successfully"})





