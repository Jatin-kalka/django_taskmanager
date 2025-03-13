#Jatin Project
# Import libraries
from django.db import models
from django.contrib.auth.models import User


# Model to extend Django's built-in User model with additional fields
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # One-to-one relationship with User model, ensuring each user has a single profile
    role = models.CharField(max_length=20, default='user')  # Defines the role of the user, defaulting to 'user' (can be admin, manager, etc.)

    def __str__(self):
        return self.user.username

# Model representing a project, associated with a user
class Project(models.Model):
    name = models.CharField(max_length=100) # Field to store the project name
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Model representing a task within a project
class Task(models.Model):
     # Predefined choices for projects, priority, and status
    PROJECT_CHOICES = [
        ('Project A', 'Project A'),
        ('Project B', 'Project B'),
        ('Project C', 'Project C'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    
    # Field to store the task title
    title = models.CharField(max_length=100)
    # Stores the name of the person responsible for handling the task
    handler_name = models.CharField(max_length=100)
    # Optional field to store additional task details
    description = models.TextField(blank=True, null=True)
    # Optional field to store the deadline for the task
    due_date = models.DateTimeField(blank=True, null=True)
    # Defines task priority (low, medium, high)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low')
     # Defines task status (pending or completed)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    # Many-to-one relationship: a task is assigned to a user
    # Deleting the user will remove all associated tasks
    user = models.ForeignKey(User, on_delete=models.CASCADE)
     # Specifies which project the task belongs to
    project = models.CharField(max_length=20, choices=PROJECT_CHOICES, default='Project A')

    def __str__(self):
        return self.title
