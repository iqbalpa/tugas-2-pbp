from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def show_todolist(request):
    username = None
    # if request.user.is_authenticated():
    #     username = request.user.username
    context = { "username":username }
    return render(request, "todolist.html", context)

def create_task(request):
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
