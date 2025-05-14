from django import forms
from .models import Task, Category

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'priority', 'category']

class FilterPriorityForm(forms.Form):
    priority_choices = [('', 'All')] + list(Task.priority_choices)
    priority = forms.ChoiceField(choices=priority_choices, required=False, label='Filter by priority')

    order_choices = [
        ('', 'Default'),
        ('date_created', 'Creation Date (oldest first)'),
        ('-date_created', 'Creation Date (newest first)'),
        ('priority_order', 'Priority (high first)'), # We will sort by our annotated field
        ('-priority_order', 'Priority (low first)'),
    ]
    order = forms.ChoiceField(
        choices=order_choices,
        required=False,
        label='Order by'
    )

class FilterCategoryForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="All categories",
        label="Filter by category")