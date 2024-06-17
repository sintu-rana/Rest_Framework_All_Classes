from django.shortcuts import render
from modelviewset.models import Student
from modelviewset.serializers import StudentSerializer
from rest_framework import viewsets

# Create your views here.


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer