from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from function_based_views.models import Employee
from function_based_views.serializers import EmployeeSerializer
from rest_framework import status

# Create your views here.


@api_view(['GET','POST'])
def employee_view(request):
    if request.method == 'GET':
        employee=Employee.objects.all()
        serializer=EmployeeSerializer(employee, many=True)
        return Response({'status':True,'msg':'Employee Data Retrieved','data':serializer.data})
    
    elif request.method == 'POST':
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':True,'msg':'Employee data is  Saved','data':serializer.data})
        else:
            return Response({'status':False,'error':serializer.errors,'data':serializer.data})
        


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def employee_detail_view(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)