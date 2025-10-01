from django.shortcuts import render, get_object_or_404
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')

def detail(request, pk):
    todos = get_object_or_404(Todo, pk=pk)
    context = {
        'todos': todos
    }
    return render(request, 'todos/detail.html', context)