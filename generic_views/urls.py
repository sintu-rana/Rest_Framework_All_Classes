from django.urls import path
from generic_views.views import *

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('books/<int:pk>/retrieve-update/', BookRetrieveUpdateView.as_view(), name='book-retrieve-update'),
    path('books/<int:pk>/retrieve-destroy/', BookRetrieveDestroyView.as_view(), name='book-retrieve-destroy'),
    path('books/<int:pk>/retrieve-update-destroy/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
]
