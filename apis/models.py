import email
from pyexpat import model
from sqlite3 import Date
from django.db import models
from django.utils import timezone

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    person = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    

    def __str__(self):
        return self.name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    present = models.CharField(max_length=10,blank=True,null=True, default='Absent')
    checkin = models.CharField(max_length=50,blank=True,null=True)
    checkout = models.CharField(max_length=50,blank=True,null=True)
    day = models.CharField(max_length=100,blank=True,null=True)
    # checkout = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employee.name 


class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(max_length=100,blank=True,null=True)
    fromdate = models.CharField(max_length=50,blank=True,null=True)
    todate = models.CharField(max_length=50,blank=True,null=True)
    request = models.CharField(max_length=50,blank=True,null=True, default='Pending')
    subday = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.employee.name 
