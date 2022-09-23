from django.urls import path
from todolist.views import show_todolist, registrasi_user, login_user, logout_user

urlpatterns = [
    path('', show_todolist, name="show_todolist"),
    path('registrasi/', registrasi_user, name="registrasi_user"),
    path('login/', login_user, name="login_user"),
    path('logout/', logout_user, name="logout_user"),
]