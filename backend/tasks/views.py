from django.shortcuts import render




from rest_framework import generics
from .models import Task
from .serializer import TaskSerializer

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task. objects.all()
    serializer_class = TaskSerializer