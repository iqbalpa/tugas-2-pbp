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
    username = request.user.username
    tasks = Task.objects.all()
    print(tasks)
    context = { 
        "username": username,
        "todolist": tasks
    }
    return render(request, "todolist.html", context)

# masih belum bisa get data dari HTML
@login_required(login_url="/todolist/login")
def create_task(request):
    if request.method == "POST":
        judul = request.POST.get("judul")
        deskripsi = request.POST.get("deskripsi")
        newTask = Task(user=request.user, title=judul, description=deskripsi, date=datetime.now())
        newTask.save()
        # Task.objects.create(
        #     user=request.user,
        #     title=judul,
        #     description=deskripsi,
        #     date=datetime.now()
        # )
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
