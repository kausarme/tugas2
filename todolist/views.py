from django.shortcuts import render
from models import Task


# Create your views here.
def show_todolist(request):
    todolist_item = Task.objects.all()
    context = {
        'list_todo': todolist_item,
        'nama': 'Kausar Meutuwah',
        'NPM': "2106630100",
    }
    return render(request, "todolist.html", context)
