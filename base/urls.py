from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/create/', views.create_task, name='create-task'),
    path('task/delete/<str:id>', views.delete_task, name='delete-task'),
]