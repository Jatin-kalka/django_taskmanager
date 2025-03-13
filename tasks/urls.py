#Jatin Project
#My Project
# Import libraries
from django.urls import path
from . import views

# Define URL patterns for the task management application

urlpatterns = [
    # URL for the home page, mapped to the `home` view
    # URL for the dashboard, where users can see their tasks (requires authentication)
    # URL for creating a new task, mapped to the `create_task` view
    # URL for deleting a specific task; expects an integer `task_id` as a parameter
    # URL for user registration, allowing new users to sign up
    # URL for user login, mapped to the `user_login` view
    # URL for logging out users, mapped to the `user_logout` view
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-task/', views.create_task, name='create_task'),
    path('update-task/<int:task_id>/', views.update_task, name='update_task'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

