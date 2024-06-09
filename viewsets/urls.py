from django.urls import path,include
from viewsets.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'libraries', LibraryViewSet, basename='library')

urlpatterns = [
    path('', include(router.urls)),
]




"""Library Endpoints: http://127.0.0.1:8000/viewsets/libraries/<id>/

GET /libraries/: Retrieve the list of all libraries.
POST /libraries/: Create a new library.
GET /libraries/<int:pk>/: Retrieve a specific library by ID.
PUT /libraries/<int:pk>/: Update a specific library by ID.
PATCH /libraries/<int:pk>/: Partially update a specific library by ID.
DELETE /libraries/<int:pk>/: Delete a specific library by ID.

"""