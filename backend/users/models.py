from django.contrib.auth.models import AbstractUser , Group, Permission
from django.db import models


class CustomerUser(AbstractUser):
    email = models.EmailField(unique = True)

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # Change related_name to avoid clash
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # Change related_name to avoid clash
        blank=True
    )
    