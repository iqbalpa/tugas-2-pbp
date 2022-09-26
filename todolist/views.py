from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime 

from todolist.models import Task

# Create your views here.
@login_required(login_url="/todolist/login")
def show_todolist(request):
    if request.method == "POST":
        task_id = request.POST.get("id")
        task = Task.objects.get(id=task_id)
        if task.is_finished:
            task.is_finished = False
        else:
            task.is_finished = True
        task.save()
        return redirect("show_todolist")
        
    username = request.user.username
    user_id = request.user.id
    tasks = Task.objects.filter(user_id=user_id)
    context = { 
        "username": username,
        "todolist": tasks
    }
    return render(request, "todolist.html", context)

@login_required(login_url="/todolist/login")
def create_task(request):
    if request.method == "POST":
        judul = request.POST.get("judul")
        deskripsi = request.POST.get("deskripsi")
        newTask = Task(user=request.user, title=judul, description=deskripsi, date=datetime.now())
        newTask.save()
        return redirect("show_todolist")
    return render(request, "create_task.html")

def registrasi_user(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful")
            return redirect("login_user")
    context = {"form":form}
    return render(request, "registration.html", context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("show_todolist")
    context = {}
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    return redirect("login_user")

def click_button(request, id):
    task = Task.objects.get(id=id)
    if task.is_finished:
        task.is_finished = False
    else:
        task.is_finished = True
    task.save()
    return render(request, "todolist.html")