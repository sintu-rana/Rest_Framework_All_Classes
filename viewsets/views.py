from django.shortcuts import render
from viewsets.models import Library
from viewsets.serializers import LibrarySerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.


class LibraryViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Library.objects.all()
        serializer = LibrarySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Library.objects.all()
        library = get_object_or_404(queryset, pk=pk)
        serializer = LibrarySerializer(library)
        return Response(serializer.data)

    def update(self, request, pk=None):
        library = get_object_or_404(Library, pk=pk)
        serializer = LibrarySerializer(library, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        library = get_object_or_404(Library, pk=pk)
        serializer = LibrarySerializer(library, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        library = get_object_or_404(Library, pk=pk)
        library.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)