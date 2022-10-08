from django.urls import path
from todolist.views import delete_task, show_todolist, registrasi_user, login_user, logout_user, create_task, delete_task, update_task
from todolist.views import show_todolist_json, add_task

app_name = "todolist"

urlpatterns = [
    path('', show_todolist, name="show_todolist"),
    path('register/', registrasi_user, name="registrasi_user"),
    path('login/', login_user, name="login_user"),
    path('logout/', logout_user, name="logout_user"),
    path('create-task/', create_task, name="create_task"), 
    path('delete/<int:id>', delete_task, name="delete_task"),
    path('update/<int:id>', update_task, name="update_task"),
    path('json/', show_todolist_json, name="show_todolist_json"),
    path('add/', add_task, name="add_task"),
]