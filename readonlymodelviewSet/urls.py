from django.urls import path,include
from readonlymodelviewSet.views import *
from rest_framework.routers import DefaultRouter

# Creating Router object
router = DefaultRouter()

# Register CollageViewSet with the Router
router.register(r'collages', CollageViewSet, basename='collage')

urlpatterns = [
    path('', include(router.urls)),
]


"""
Collage Endpoints:- http://127.0.0.1:8000/readonlymodelviewSet/collages/1/

GET /api/collages/: Retrieve the list of all collages.
GET /api/collages/int:pk/: Retrieve a specific collage by ID.

"""