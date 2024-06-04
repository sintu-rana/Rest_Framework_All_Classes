# All Django Rest framework Classes (rest_framework_all_classes)

## apps in this project

### 1.function_based_views
### 2.generic_views
### 3.viewsets----
### 4.modelviewset---
### 5.readonlymodelviewSet---
### 6.mixin_api


## 1.Function-Based Views (FBVs):-

Function-Based Views (FBVs) in Django are views that are implemented as simple Python functions. They are a straightforward and intuitive way to handle web requests and responses. Each function corresponds to a specific URL pattern and is responsible for handling one or more HTTP methods (e.g., GET, POST, PUT, DELETE). FBVs provide a flexible and readable way to define the logic for your views, especially for smaller and simpler projects.

#### GET /employees/: Retrieve the list of all employees.
#### POST /employees/: Create a new employee.
---------------------------------------------
#### GET /employees/<int:pk>/: Retrieve a specific employee by ID.
#### PUT /employees/<int:pk>/: Update a specific employee by ID (replace all fields).
#### PATCH /employees/<int:pk>/: Partially update a specific employee by ID.
#### DELETE /employees/<int:pk>/: Delete a specific employee by ID.

## 2.Generic Views:-

Generic Views are class-based views provided by DRF that reduce the amount of code you need to write by providing common patterns for creating API views. They handle basic operations like create, retrieve, update, and delete. Here are a few examples:

#### CreateAPIView
#### ListAPIView
#### RetrieveAPIView
#### UpdateAPIView
#### DestroyAPIView
#### ListCreateAPIView
#### RetrieveUpdateAPIView
#### RetrieveDestroyAPIView
#### RetrieveUpdateDestroyAPIView



## 3.Viewsets:- 

Viewsets are a type of class-based view provided by DRF that allow you to group together related views (e.g., CRUD operations) for a set of related resources. Instead of defining multiple views for listing, creating, retrieving, updating, and deleting resources, you can define a single viewset.

##### There are different types of viewsets:

#### 1.ViewSet
#### 2.ModelViewSet
#### 3.ReadOnlyModelViewSet

---------------------------

## 4.Mixins API View:-

Mixins are small reusable components that can be combined to create class-based views. DRF provides a set of mixins for common operations which can be used to add specific behaviors to views. The most commonly used mixins include:

#### CreateModelMixin
#### UpdateModelMixin
#### DestroyModelMixin
#### ListModelMixin
#### RetrieveModelMixin