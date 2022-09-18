
from django.shortcuts import render
from .models import Attendance, Employee, Leave
from .serializers import EmployeeSerializer,AttendanceSerializer, LeaveSerializer
from django.http import HttpResponse

#for restframework usage as respones instead of json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#for class based views
from rest_framework.views import APIView

from django.db.models import Q
from datetime import date




class Login(APIView):

    def get(self,request,n,p):
        try:
            employee = Employee.objects.get(Q(email=n) & Q(password=p))
        except:
            employee=''

        if employee:
            serializer = EmployeeSerializer(employee)

            all = Attendance.objects.filter(employee=employee)
            check = False

            for a in all:
                if a.day == str(date.today()):
                    check = True

            if not check:
                a = Attendance.objects.create(
                        employee=employee,
                        present = 'Present',
                        day = str(date.today())
                        )
            return Response(serializer.data)

        return HttpResponse(employee) 

class EmployeeList(APIView):
    
    def get(self,request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):

    def getobject(self, pk):
        try:
            return Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        employee = self.getobject(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = self.getobject(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.getobject(pk)
        employee.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT) 

class AttendanceList(APIView):
    
    def get(self,request):
        attendance = Attendance.objects.all()
        serializer = AttendanceSerializer(attendance,many=True)
        return Response(serializer.data)

    def post(self,request):

        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AttendanceDetail(APIView):

    def getobject(self, pk):
        try:
            employee = Employee.objects.get(id=pk)
            return Attendance.objects.get(Q(employee=employee) & Q(day=date.today()))
        except Attendance.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        attendance = self.getobject(pk)
        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data)

    def put(self, request, pk):
        attendance = self.getobject(pk)

        datain = request.POST.get('checkin')
        dataout = request.POST.get('checkout')

        if datain:
            if attendance.checkin is None:
                serializer = AttendanceSerializer(attendance, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
        
        if dataout:
             if attendance.checkout is None:
                serializer = AttendanceSerializer(attendance, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)

        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data)

    def delete(self, request, pk):
        attendance = self.getobject(pk)
        attendance.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT) 

class LeaveDetail(APIView):

    def getobject(self, pk):
        try:
            employee = Employee.objects.get(id=pk)
            return Leave.objects.all().filter(employee=employee)
        except Leave.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        leave = self.getobject(pk)
        serializer = LeaveSerializer(leave,many=True)
        return Response(serializer.data)

class LeavePutDelete(APIView):
    
    def getobject(self, pk):
        try:
            return Leave.objects.get(id=pk)
        except Leave.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        leave = self.getobject(pk)
        serializer = LeaveSerializer(leave, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Leave = self.getobject(pk)
        Leave.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT) 

class LeaveList(APIView):
    
    def get(self,request):
        leave = Leave.objects.all()
        serializer = LeaveSerializer(leave,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = LeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ManagerDetail(APIView):

    def getobject(self, pk):
        try:
            return Manager.objects.get(id=pk)
        except Manager.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        employee = self.getobject(pk)
        serializer = ManagerSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = self.getobject(pk)
        serializer = ManagerSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.getobject(pk)
        employee.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT) 








# @api_view(['PUT','POSt'])
# def attendanceDetail(request, pk):
#     employee = Employee.objects.get(id=pk)
#     attendance =  Attendance.objects.get(Q(employee=employee) & Q(day=date.today()))

#     serializer = AttendanceSerializer(attendance, data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    # try:
    #     employee = Employee.objects.get(id=pk)
    #     attendance =  Attendance.objects.get(Q(employee=employee) & Q(day=date.today()))
    # except Attendance.DoesNotExist:
    #     return HttpResponse(status=status.HTTP_404_NOT_FOUND)


    # if request.method == 'GET':
    #     serializer = AttendanceSerializer(attendance)
    #     return Response(serializer.data)


    # elif request.method == 'POST':   #put means update
    #     serializer = AttendanceSerializer(attendance, data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     attendance.delete()
    #     return HttpResponse(status=status.HTTP_204_NO_CONTENT) 

