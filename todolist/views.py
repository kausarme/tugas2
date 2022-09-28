from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from todolist.forms import TaskForm
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        "user": request.user,
    }
    return render(request, "todolist.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('todolist:login')


@login_required(login_url="/todolist/login/")
def create_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect("/todolist")

    context = {
        "form": form,
    }

    return render(request, "create_task.html", context)


@login_required(login_url="/todolist/login/")
def delete_task(request, id):
    task = Task.objects.get(pk=id)
    if task:
        task.delete()
        return redirect("/todolist")
    messages.error(request, "An error occurred while deleting the task.")
    return redirect("/todolist")


@login_required(login_url="/todolist/login/")
def toggle_task(request, id):
    task = Task.objects.get(pk=id)
    if task:
        task.is_finished = False if task.is_finished else True
        task.save()
        return redirect("/todolist")
    messages.error(request, "An error occurred while editing the task.")
    return redirect("/todolist")