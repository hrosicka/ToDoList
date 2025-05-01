from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddTaskForm, FilterPriorityForm, FilterCategoryForm
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
    priority_filter_form = FilterPriorityForm(request.GET)
    category_filter_form = FilterCategoryForm(request.GET)
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

    if priority_filter_form.is_valid():
        priority_filter = priority_filter_form.cleaned_data.get('priority')
        if priority_filter:
            tasks = tasks.filter(priority=priority_filter)
            if order:
                tasks = tasks.order_by(order)
            else:
                tasks = tasks.order_by('priority_order')

    if category_filter_form.is_valid():
        category_filter = category_filter_form.cleaned_data.get('category')
        if category_filter:
            tasks = tasks.filter(category=category_filter)
            if order:
                tasks = tasks.order_by(order)
            else:
                tasks = tasks.order_by('priority_order')

    context = {
        'tasks': tasks,
        'priority_filter_form': priority_filter_form,
        'category_filter_form': category_filter_form,
    }
    return render(request, 'todolist/task_list.html', context)

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
            return redirect('task_list')
    else:
        form = AddTaskForm(instance=task)
    return render(request, 'todolist/edit_task.html', {'form': form, 'task': task})