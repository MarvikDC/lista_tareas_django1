from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('complete/<int:pk>/', views.task_complete, name='task_complete'),
    path('edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
]