from django.urls import path
from .views import ListTodo, DetailTodo

urlpatterns = [
    path('', ListTodo.as_view()),
    path('todos/<int:pk>/', DetailTodo.as_view()),
]