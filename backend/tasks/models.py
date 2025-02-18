

# # Create your models here.

# from django.db import models
# from users.models import CustomUser

# class Task(models.Model):
#     title = models. CharField(max_length=255)
#     description = models. TextField()
#     assigned_to = models. ForeignKey(CustomUser, on_delete=models)

# Create your models here.

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)  # Fix circular import and add appropriate on_delete behavior
