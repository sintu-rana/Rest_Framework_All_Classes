from django.urls import path,include
from modelviewset.views import *
from rest_framework.routers import DefaultRouter

# Creating Router object
router = DefaultRouter()

# Register StudentViewSet with the Router
router.register(r'students', StudentViewSet, basename='student')


urlpatterns = [
    path('', include(router.urls)),  # Including router-generated URLs
]


""""
Student EndPoints:-  http://127.0.0.1:8000/admin/modelviewset/student/<id>/

GET /api/students/: Retrieve the list of all students.
POST /api/students/: Create a new student.
GET /api/students/int:pk/: Retrieve a specific student by ID.
PUT /api/students/int:pk/: Update a specific student by ID (replace all fields).
PATCH /api/students/int:pk/: Partially update a specific student by ID.
DELETE /api/students/int:pk/: Delete a specific student by ID

"""