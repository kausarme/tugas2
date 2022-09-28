from django.urls import path
from todolist.views import show_todolist, register

app_name = "todolist"

urlpatterns = [
    path("", show_todolist, name="show_todolist"),
    path("register/", register, name="register"),
]