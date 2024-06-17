from django.shortcuts import render
from readonlymodelviewSet.models import Collage
from readonlymodelviewSet.serializers import CollageSerializer
from rest_framework import viewsets

# Create your views here.

class CollageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Collage.objects.all()
    serializer_class = CollageSerializer