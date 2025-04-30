from django import forms
from .models import Task

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'priority']

class FilterPriorityForm(forms.Form):
    priority = forms.ChoiceField(
        choices=[('', 'All')] + Task.priority_choices,
        required=False,
        label='Filtrovat podle priority'
    )