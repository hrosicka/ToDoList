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
    order_choices = [
        ('', 'Default'),
        ('date_created', 'Datum vytvoření (nejstarší první)'),
        ('-date_created', 'Datum vytvoření (nejnovější první)'),
        ('priority_order', 'Priorita (vysoká první)'), # Budeme řadit podle našeho anotovaného pole
        ('-priority_order', 'Priorita (nízká první)'),
    ]
    order = forms.ChoiceField(
        choices=order_choices,
        required=False,
        label='Řadit podle'
    )