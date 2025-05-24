from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def about(request):
    return render(request, 'about.html')

def create(request):
    error = 'Ты что то сделал не так, попробуй еще раз'
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', context)

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')