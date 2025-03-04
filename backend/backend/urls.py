"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# from django.urls import path
# from users.views import UserListCreate
# from tasks.views import TaskListCreate

# urlpatterns = [
# path('users/', UserListCreate.as_view(), name='users-list'),
# path('tasks/', TaskListCreate.as_view(), name='tasks-list'),

# ]

# from django.contrib import admin
# from django.urls import path
# from users.views import UserListCreate
# # from tasks.views import TaskListCreate

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/users/', UserListCreate.as_view(), name='users-list'),
#     # path('api/tasks/', TaskListCreate.as_view(), name='tasks-list'),
# ]

# ---------------

# from django.urls import path
# from tasks.views import TaskListCreateView, TaskDetailView

# urlpatterns = [
#     path('api/tasks/', TaskListCreateView.as_view(), name='tasks-list'),
#     path('api/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),  # CRUD for single task
# ]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),  # Include users API
    path('api/', include('tasks.urls')),  # Include tasks API
]
