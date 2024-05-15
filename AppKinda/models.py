from django.db import models

# Create your models here.

class Position(models.Model):
    name=models.CharField(max_length=40)

class Employee(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    contract_date=models.DateField()
    position=models.ForeignKey(Position, on_delete=models.CASCADE)
    
class Cars(models.Model):
    name=models.CharField(max_length=40)
    price=models.IntegerField()
    color=models.CharField(max_length=40)
    image = models.CharField(max_length=100) 
    description = models.CharField(max_length=255)

class Client(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    phone=models.CharField(max_length=40)
    address=models.CharField(max_length=40)