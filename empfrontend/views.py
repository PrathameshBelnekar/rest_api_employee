import requests
from django.shortcuts import redirect, render



def EmpList(request):
    url = "http://127.0.0.1:8000/employees/"

    response = requests.get(url)
    if response.status_code == 200:
        emp_data = response.json()
        # print(emp_data)
        context = {'emp_data': emp_data}
        return render(request, 'empfrontend/listemployee.html', context)


def EmpDetail(request, pk):
    url = f"http://127.0.0.1:8000/employee/{pk}/"
    response = requests.get(url)
    if response.status_code == 200:
        emp_data = response.json()
        # print(emp_data)
        context = {'emp_data': emp_data}
        return render(request, 'empfrontend/detailemployee.html', context)
    


def EmpCreate(request):
    if request.method == 'GET':
        return render(request, 'empfrontend/addemployees.html')
    elif request.method == 'POST':
        url = "http://127.0.0.1:8000/employees/"

        emp_data = {
            'emp_name': request.POST.get('emp_name'),
            'joining_date': request.POST.get('joining_date'),
            "salary": request.POST.get("salary"),
        }

        response = requests.post(url, data = emp_data)
        return redirect('employee-list-front')



def EmpUpdate(request, pk):
    url = f"http://127.0.0.1:8000/employee/{pk}/"
    if request.method == 'GET':
        response_get = requests.get(url) 
        json_data = response_get.json()
        # print(json_data)
        return render(request,'empfrontend/updateemployees.html',{'emp_data': json_data})
    elif request.method == 'POST':
        emp_data = {
            'emp_name': request.POST.get('emp_name'),
            'joining_date': request.POST.get('joining_date'),
            "salary": request.POST.get("salary"),
            
        }
        
        response = requests.put(url, json= emp_data)
        
        return redirect('employee-list-front')



def DeleteInactive(request):
    url = 'http://127.0.0.1:8000/updatedeletesalary/'
    response = requests.delete(url)
    return redirect('employee-list-front')




def UpdateSalary(request):
    url = 'http://127.0.0.1:8000/updatedeletesalary/'
    response = requests.put(url)
    print(response.text)

    return redirect('employee-list-front')




def UpdateStatus(request,pk):
    url = f"http://127.0.0.1:8000/employee/{pk}/"
    
    response_get = requests.get(url)
    json_data = response_get.json()
    print(json_data['status'])
    if json_data['status'] == 'Active':
        status_data = {"status" : "Deactive"}
        response_data = requests.put(url, json=status_data)
        print(response_data.text)
        
    else:
        status_data ={"status" : "Active"} 
        response_data = requests.put(url, json=status_data)
        

    return redirect('employee-list-front')

