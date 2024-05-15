from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from AppKinda.forms import *
from AppKinda.models import *

def employee(request):

    positions = Position.objects.all()
    employees = Employee.objects.all()
    
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST)
        
        if employee_form.is_valid():
            data = employee_form.cleaned_data
            position = Position.objects.get(pk=2)
            new_employee = Employee(
                name=data['name'],
                email=data['email'],
                contract_date=data['contract_date'],
                position=position
            )
            
            new_employee.save()
            
            return render(request, 'AppKinda/index.html', {"message_success":'Añadido correctamente.'})
    else:
        employee_form = EmployeeForm()
        
    return render(request, 'AppKinda/Employee.html', {'employeeForm':employee_form, 'positions':positions, 'employees':employees})

def clients(request):
    
    if request.method == 'POST':
        client_form = ClientsForm(request.POST)
        
        if client_form.is_valid():
            data = client_form.cleaned_data
            
            new_client = Client(
                name=data['name'],
                email=data['email'],
                phone=data['phone'],
                address=data['address']
            )
            
            new_client.save()
            
            return render(request, 'AppKinda/index.html', {"message_success":'Añadido correctamente.'})
    else:
        client_form = ClientsForm()
    
    return render(request, 'AppKinda/clients.html', {'clientForm':client_form})
    
def cars(request):
    
    if request.method == 'POST':
        car_form = CarsForm(request.POST)
       
        if car_form.is_valid():
            cleaned_data = car_form.cleaned_data
           
            new_car = Cars(
                name=cleaned_data['name'],
                price=cleaned_data['price'],
                color=cleaned_data['color'],
                image=cleaned_data['image'],
                description=cleaned_data['description']
            )
            new_car.save()
            
            return render(request, 'AppKinda/index.html', {"message_success":'Añadido correctamente.'})
    else:
        car_form = CarsForm()
    
    return render(request, 'AppKinda/cars.html', {'carsForm': car_form})
    
def index(request):
    cars = Cars.objects.all()
    
    return render(request, 'AppKinda/index.html', {'cars':cars})

def search_car(request):
    
    if request.GET['search_value']:
        search_value = request.GET['search_value']
        cars = Cars.objects.filter(name__icontains=search_value)
        
        return render(request, 'AppKinda/index.html', {'cars':cars}) 
    else:
        cars = Cars.objects.all()
    
    return render(request, 'AppKinda/index.html', {'cars':cars, 'message_search':'No se envío ningún valor'}) 