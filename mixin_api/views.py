from django.shortcuts import render
from mixin_api.models import Employee
from mixin_api.serialzers import EmployeeSerializer
from rest_framework import viewsets, mixins

# Create your views here.


class EmployeeViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
