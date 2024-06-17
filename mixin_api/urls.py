from django.urls import path,include
from mixin_api.views import *
from rest_framework.routers import DefaultRouter

# Creating Router object
router = DefaultRouter()

# Register EmployeeViewSet with the Router
router.register(r'employees', EmployeeViewSet, basename='employee')


urlpatterns = [
    path('', include(router.urls)),  # Including router-generated URLs
]


"""
Employee Endpoints:- http://127.0.0.1:8000/mixin_api/employees/2/

GET /api/employees/: Retrieve the list of all employees.
POST /api/employees/: Create a new employee.
GET /api/employees/int:pk/: Retrieve a specific employee by ID.
PUT /api/employees/int:pk/: Update a specific employee by ID (replace all fields).
PATCH /api/employees/int:pk/: Partially update a specific employee by ID.
DELETE /api/employees/int:pk/: Delete a specific employee by ID.

"""