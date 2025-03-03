# from django.shortcuts import render

# # Create your views here.
# from rest_framework import generics
# from .models import CustomUser
# from .serializer import UserSerializer

# class UserListCreate(generics.ListCreateAPIView):
#     queryset = CustomUser. objects. all()
#     serializer_class = UserSerializer

from rest_framework import generics
from .models import CustomUser
from .serializer import UserSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
