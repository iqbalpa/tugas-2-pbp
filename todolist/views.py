from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from todolist.models import Task

# Create your views here.
def show_todolist(request):
    username = None
    todolist_data = Task.objects.all()
    # if request.user.is_authenticated():
    #     username = request.user.username
    context = { 
        "username": username,
        "todolist": todolist_data
    }
    return render(request, "todolist.html", context)

def create_task(request):
    if request.method == "POST":
        judul = request.POST.get("judul")
        deskripsi = request.POST.get("deskripsi")
        user = request.user
        new_task = Task(user=user, title=judul, description=deskripsi)
        new_task.save()
    return render(request, "create_task.html")

def registrasi_user(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful")
            return redirect("todolist:login")
    context = {"form":form}
    return render(request, "registration.html", context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("todolist:show_todolist")
    context = {}
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    return redirect("todolist:login")
