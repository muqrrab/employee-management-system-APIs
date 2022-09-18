from datetime import date
from http.client import HTTPResponse
from re import A
from urllib import response
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
import json

def login(request):
    context={}
    return render(request,'ems/index.html',context)

# def login(request,n,p):
#     data = requests.get(f'http://127.0.0.1:8000/ems/{n}/{p}/')
#     print(data.json())
#     return HTTPResponse('Ok')
#     # return render(request,'ems/index.html')

def signup(request):
    context={}
    return render(request,'ems/signup.html',context)

# @login_required(login_url='login')
def dashboard(request,id):
    employee = requests.get("http://127.0.0.1:8000/api/ems/"+str(id))
   
    try:
        a = requests.get("http://127.0.0.1:8000/api/ems/attendance/"+str(id))
    except:
        a=''


    data = employee.json()
    context={'e':data,'date':date.today(),'a':a.json()}
    

    if data['person'] == 'Employee':
        return render(request,'ems/employee.html',context)
    else:
        return render(request,'ems/manager.html',context)

