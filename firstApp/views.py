from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import User, Task


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    data = {
        'title': 'Добро пожаловать на главную страницу!',
        'users': 'Пользователи',
        'tasks': 'Задачи',
        'test': 'Тестовая версия добавления юзеров и задач',
        'reguser': 'Добавление пользователя',
        'regtask': 'Добавление задачи'

    }
    return render(request, 'home.html', context=data)


def users(request: HttpRequest) -> HttpResponse:
    data = User.objects.all().values()
    users = {
        'head': 'Пользователи',
        'user': data,
    }
    return render(request, 'users.html', context=users)


def tasks(request: HttpRequest) -> HttpResponse:
    data = Task.objects.all().values()
    tasks = {
        'head': 'Задачи',
        'task': data,
    }
    return render(request, 'tasks.html', context=tasks)


def reg_user(request: HttpRequest) -> HttpResponse:
    try:
        user = User(name='Alex', lastname='Kamenski', age=20, phone=375441234567, address='Minsk')
        user.save()
        return HttpResponse("OK")
    except:
        return HttpResponse("Error")


def reg_task(request: HttpRequest) -> HttpResponse:
    try:
        task = Task(name='Сходить на работу', deadline=1)
        task.save()
        return HttpResponse("OK")
    except:
        return HttpResponse("Error")


def get_user_id(request: HttpRequest, id: int) -> HttpResponse:
    data = User.objects.all().values()
    use = {
        'id': id,
        'head': 'Информация о пользователе',
        'user': data,
    }
    return render(request, 'usersid.html', context=use)


def get_task_id(request: HttpRequest, id: int) -> HttpResponse:
    data = Task.objects.all().values()
    tas = {
        'id': id,
        'head': 'Информация о задаче',
        'task': data,
    }
    return render(request, 'tasksid.html', context=tas)
