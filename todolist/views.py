from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddTaskForm
from .models import Task

def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Přesměrujeme na stránku se seznamem úkolů
    else:
        form = AddTaskForm()

    return render(request, 'todolist/add_task.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todolist/task_list.html', {'tasks': tasks})

def tag_resolved(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.resolved = True
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('task_list')

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = AddTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('seznam_ukolu')
    else:
        form = AddTaskForm(instance=task)
    return render(request, 'todolist/edit_task.html', {'form': form, 'task': task})