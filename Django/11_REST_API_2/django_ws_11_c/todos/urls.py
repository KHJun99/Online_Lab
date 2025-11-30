from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/<int:todo_pk>/', views.todo_detail, name='todo_detail'),
    path('todos/<int:todo_pk>/recommends/', views.recommend_create, name='recommend_create'),
]