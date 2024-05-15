from django import forms
from AppKinda.models import *

class EmployeeForm(forms.Form):
    name=forms.CharField(max_length=40)
    email=forms.EmailField()
    contract_date=forms.DateField()
    position=forms.IntegerField()
    
class ClientsForm(forms.Form):
    name=forms.CharField(max_length=40)
    email=forms.EmailField()
    phone=forms.CharField(max_length=40)
    address=forms.CharField(max_length=40)
    
class CarsForm(forms.Form):
    name=forms.CharField(max_length=40)
    price=forms.IntegerField()
    color=forms.CharField(max_length=40)
    image = forms.CharField(max_length=100) 
    description = forms.CharField(max_length=255)