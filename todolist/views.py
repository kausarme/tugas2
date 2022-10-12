from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from todolist.forms import TaskForm
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core import serializers
import datetime

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    tasks = Task.objects.filter(user=request.user)
    context = {
        'tasks': tasks,
        "user": request.user,
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def show_todolist_lama(request):
    tasks = Task.objects.filter(user=request.user)
    context = {
        'tasks': tasks,
        "user": request.user,
    }
    return render(request, "todolist_backup.html", context)

@login_required(login_url='/todolist/login/')
def show_todolist_json(request):
    data_task = Task.objects.filter(user=request.user).order_by('id')
    return HttpResponse(serializers.serialize("json", data_task), content_type="application/json")


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
    task = Task.objects.filter(pk=id, user=request.user).first()
    if task:
        task.delete()
        return redirect("/todolist")
    messages.error(request, "An error occurred while deleting the task.")
    return redirect("/todolist")


@login_required(login_url="/todolist/login/")
def toggle_task(request, id):
    task = Task.objects.filter(pk=id, user=request.user).first()
    if task:
        task.is_finished = False if task.is_finished else True
        task.save()
        return redirect("/todolist")
    messages.error(request, "An error occurred while editing the task.")
    return redirect("/todolist")


@login_required(login_url='/todolist/login/')
def add_task(request):
    if request.method != 'POST':
        return redirect('todolist:todolist')

    form = TaskForm(request.POST)
    if form.is_valid():
        new_task = form.save(commit=False)
        new_task.user = request.user
        new_task.date = datetime.datetime.now()
        new_task.save()
        form.save_m2m()
        return JsonResponse({
            'pk' : new_task.pk,
            'date' : new_task.date,
            'title' : new_task.title,
            'description' : new_task.description,
            'is_finished' : new_task.is_finished
        })
