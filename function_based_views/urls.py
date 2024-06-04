from django.urls import path
from function_based_views.views import *

urlpatterns = [
    path('employees/',employee_view, name='employee'),
    path('employees/<int:pk>/', employee_detail_view, name='employee-detail'),

]
