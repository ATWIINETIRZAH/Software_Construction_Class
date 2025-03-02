# from django.shortcuts import render




# from rest_framework import generics
# from .models import Task
# from .serializer import TaskSerializer

# class TaskListCreate(generics.ListCreateAPIView):
#     queryset = Task. objects.all()
#     serializer_class = TaskSerializer

# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter, OrderingFilter

# class TaskListCreateView(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     filterset_fields = ['assigned_to']
#     search_fields = ['title', 'description']
#     ordering_fields = ['created_at']


from rest_framework import generics
from .models import Task
from .serializer import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# List and Create
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['assigned_to']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']

# Retrieve, Update, Delete
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
