from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddTaskForm, FilterPriorityForm
from .models import Task
from django.db.models import Case, When, Value, IntegerField

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
    filter_form = FilterPriorityForm(request.GET)
    tasks = Task.objects.annotate(
        priority_order=Case(
            When(priority='height', then=Value(1)),
            When(priority='middle', then=Value(2)),
            When(priority='low', then=Value(3)),
            default=Value(3),
            output_field=IntegerField(),
        )
    )
    order = request.GET.get('order')
    if order:
        tasks = tasks.order_by(order)
    else:
        tasks = tasks.order_by('priority_order')

    if filter_form.is_valid():
        priority_filter = filter_form.cleaned_data.get('priority')
        if priority_filter:
            tasks = tasks.filter(priority=priority_filter)
            if order:
                tasks = tasks.order_by(order)
            else:
                tasks = tasks.order_by('priority_order')

    return render(request, 'todolist/task_list.html', {'tasks': tasks, 'filter_form': filter_form})

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