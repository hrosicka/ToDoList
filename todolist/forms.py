from django import forms
from .models import Task, Category

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'priority', 'category']

class FilterPriorityForm(forms.Form):
    priority_choices = [('', 'All')] + list(Task.priority_choices)
    priority = forms.ChoiceField(choices=priority_choices, required=False, label='Filtrovat podle priority')

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

class FilterCategoryForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), 
        required=False,
        empty_label="Všechny kategorie",
        label="Filtrovat podle kategorie")