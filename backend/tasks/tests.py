from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.contrib.auth import get_user_model  # Ensure you're using the right user model
from .models import Task

User = get_user_model()  # Dynamically get CustomUser or default User model

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")  # Use CustomUser
        self.task = Task.objects.create(title="Test Task", description="Task description", assigned_to=self.user)

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.assigned_to.username, "testuser")  # Ensure correct assignment