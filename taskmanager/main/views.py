from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def price(request):
    return render(request, 'main/price.html')

def contacts(request):
    return render(request, 'main/contacts.html')
