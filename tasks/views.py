#Jatin Project
# Import libraries
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Task, UserProfile
from .forms import TaskForm
from django.http import JsonResponse
from django.contrib import messages

#Home page
def home(request):
    return render(request, 'tasks/home.html')

#dashboard view
@login_required
def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            tasks = Task.objects.all()  # Admin sees all tasks
        else:
            tasks = Task.objects.filter(user=request.user)  # Standard user sees only their tasks

        return render(request, 'tasks/dashboard.html', {'tasks': tasks})
    else:
        return redirect('login')
    
# Create a new task - Restricted to logged-in users
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})
#My Project
# Update an existing task - Restricted to the owner or an admin
@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.user != task.user and not request.user.is_superuser:
        return redirect('dashboard')
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/update_task.html', {'form': form})
# Delete a task - Restricted to the  an admin
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.user != task.user and not request.user.is_superuser:
        return JsonResponse({"error": "Unauthorized"}, status=403)

    if request.method == "POST":
        task.delete()
        return JsonResponse({"success": True})

    return JsonResponse({"error": "Invalid request"}, status=400)

# User Registration View
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'tasks/register.html')

# User Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'tasks/login.html', {'error': 'Invalid credentials'})
    return render(request, 'tasks/login.html')

# User Logout View - Restricted to logged-in users
@login_required
def user_logout(request):
    logout(request)
    return redirect('home')
