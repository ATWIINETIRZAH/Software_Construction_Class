

from django.urls import path
from .views import UserListCreate, UserDetailView

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='users-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # CRUD for single user
]
