from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def index(request):
    todo_list = Todo.objects.all()
    return render(request, 'todos/index.html', {'todo_list': todo_list})

def create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            # ❌ 템플릿 파일명으로 redirect 하지 말 것
            # ✅ URL name으로 redirect
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm()
    return render(request, 'todos/create.html', {'form': form})

def detail(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    return render(request, 'todos/detail.html', {'todo': todo})

def delete(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    if request.method == "POST":
        todo.delete()
        return redirect('todos:index')
    # GET으로 오면 상세로 돌려보내기
    return redirect('todos:detail', todo.pk)

def update(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/update.html', {'todo': todo, 'form': form})
