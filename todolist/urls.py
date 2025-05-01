from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_task, name='add_task'),
    path('', views.task_list, name='task_list'),
    path('resolved/<int:task_id>/', views.tag_resolved, name='tag_resolved'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('editovat/<int:task_id>/', views.edit_task, name='edit_task'),
    path('export/csv/', views.export_tasks_csv, name='export_tasks_csv'),
]