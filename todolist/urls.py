from django.urls import path
from todolist.views import show_todolist

app_name = "todolist"

urlpatterns = [
    path("", show_todolist, name="show_todolist"),
]