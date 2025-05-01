from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    description = models.CharField(max_length=200)
    resolved = models.BooleanField(default=False)
    priority_choices = [
        ('height', 'Height'),
        ('middle', 'Middle'),
        ('low', 'Low'),
    ]

    priority = models.CharField(
        max_length=10,
        choices=priority_choices,
        default='stredni',
    )

    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.popis